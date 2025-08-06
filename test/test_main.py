import pytest

# Import Test Classes
from .api.test_client import APIClientTests


def test_root_endpoint(client):
    """Test para el endpoint raíz"""
    # Crear la instancia y ejecutar el test directamente
    api_tests = APIClientTests()
    api_tests.test_read_root(client)
