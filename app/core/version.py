"""Version management - Single source of truth from pyproject.toml"""

from importlib.metadata import PackageNotFoundError, version


def get_version() -> str:
    """Read version from installed package metadata."""
    try:
        return version("api-docker-service")
    except PackageNotFoundError:
        return "0.0.0"


__version__ = get_version()
