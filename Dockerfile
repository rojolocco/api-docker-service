# Multi-stage Dockerfile for FastAPI production deployment with uv
FROM python:3.13-slim AS builder

# Pin uv version for reproducibility
COPY --from=ghcr.io/astral-sh/uv:0.6.3 /uv /bin/uv

# Build-time env: compile bytecode, copy mode, no Python downloads
ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PYTHON_DOWNLOADS=never

WORKDIR /app

# Install dependencies (separate layer — cached unless pyproject/lockfile change)
COPY pyproject.toml uv.lock ./
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project --no-dev

# Copy app code and install project
COPY README.md ./
COPY ./app ./app
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

# ---------------------------------------------------------------------------
# Production stage — no uv needed at runtime
# ---------------------------------------------------------------------------
FROM python:3.13-slim

# Runtime env: activate venv via PATH, force production mode
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH" \
    API_ENV=production

# Non-root user
RUN groupadd -r appuser && useradd -r -g appuser appuser

WORKDIR /app

# Copy only the virtual environment and app code from builder
COPY --from=builder --chown=appuser:appuser /app/.venv /app/.venv
COPY --chown=appuser:appuser ./app ./app

USER appuser

EXPOSE 8000

# fastapi CLI is installed in .venv — no uv needed
CMD ["fastapi", "run", "app/main.py", "--host", "0.0.0.0", "--port", "8000"]
