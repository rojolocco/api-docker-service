import pytest
from fastapi.testclient import TestClient
from app.main import app

# Import the test client fixture from conftest.py
from .conftest import client 

# Import Test Classes
from .api.test_client import TestClient

# Create instances of Test Classes
client_tests = TestClient()

# Group all tests in a single function 
def test_all(client):
    # Execute the test for the root endpoint
    client_tests.test_read_root(client)
