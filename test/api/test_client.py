import pytest

class TestClient:

    def test_read_root(self, client):
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello Datapulse!!"}
