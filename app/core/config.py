"""Core configuration settings."""

from pydantic import ConfigDict, field_validator
from pydantic_settings import BaseSettings

from app.core.version import __version__


class Settings(BaseSettings):
    """Application settings."""

    # Environment
    API_ENV: str = "development"

    # API metadata
    API_TITLE: str = "api-docker-service"
    API_VERSION: str = __version__
    API_DESCRIPTION: str = "Template for a FastAPI service running in Docker."

    # Logging
    LOG_LEVEL: str = "INFO" # "DEBUG" | "INFO" | "WARNING" | "ERROR" | "CRITICAL"
    LOG_FORMAT: str = "json"  # "json" | "text"

    model_config = ConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )

    @field_validator("LOG_LEVEL")
    @classmethod
    def validate_log_level(cls, v: str) -> str:
        allowed = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}
        upper = v.upper()
        if upper not in allowed:
            raise ValueError(f"LOG_LEVEL must be one of {allowed}")
        return upper

    @property
    def is_production(self) -> bool:
        return self.API_ENV.lower() == "production"

    @property
    def is_development(self) -> bool:
        return self.API_ENV.lower() == "development"

    @property
    def docs_enabled(self) -> bool:
        return not self.is_production


# Global settings instance
settings = Settings()
