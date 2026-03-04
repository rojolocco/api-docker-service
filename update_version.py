#!/usr/bin/env python3
"""Script to update the version across the project.

This script updates the version in pyproject.toml and docker-compose.yaml.
All other files automatically read from pyproject.toml.

Usage:
    python update_version.py 0.2.0
"""
import re
import sys
from pathlib import Path


def update_version(new_version: str):
    """Update version in all necessary files."""

    # Validate version format (semver)
    if not re.match(r"^\d+\.\d+\.\d+$", new_version):
        print(
            f"Error: Invalid version format '{new_version}'. Use semver (e.g., 0.2.0)"
        )
        sys.exit(1)

    # Update pyproject.toml
    pyproject_path = Path("pyproject.toml")
    content = pyproject_path.read_text(encoding="utf-8")
    content = re.sub(
        r'version = "[^"]+"', f'version = "{new_version}"', content, count=1
    )
    pyproject_path.write_text(content, encoding="utf-8")
    print(f"✓ Updated pyproject.toml to {new_version}")

    # Update docker-compose.yaml
    docker_compose_path = Path("docker-compose.yaml")
    content = docker_compose_path.read_text(encoding="utf-8")
    content = re.sub(
        r"ghcr\.io/rojolocco/api-docker-service:[^\s]+",
        f"ghcr.io/rojolocco/api-docker-service:{new_version}",
        content,
    )
    docker_compose_path.write_text(content, encoding="utf-8")
    print(f"✓ Updated docker-compose.yaml to {new_version}")

    print(f"\n✅ Version updated to {new_version}")
    print("\nNext steps:")
    print("  1. uv sync          → regenerate uv.lock and update installed metadata")
    print("  2. git commit + tag → git tag v" + new_version)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python update_version.py <new_version>")
        print("Example: python update_version.py 0.2.0")
        sys.exit(1)

    update_version(sys.argv[1])
