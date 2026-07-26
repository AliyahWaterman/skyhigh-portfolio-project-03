"""Simple smoke test for the /health endpoint."""
from app import app


def test_health_returns_ok():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_info_returns_service_name():
    client = app.test_client()
    response = client.get("/api/info")
    assert response.status_code == 200
    assert response.get_json()["service"] == "skyhigh-backend"

    

