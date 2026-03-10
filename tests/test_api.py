from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200

    data = response.json()

    assert "message" in data
    assert data["message"] == "Futurisys ML API"
    assert "environment" in data


def test_prediction_valid():
    data = [1, 2, 3, 4]

    response = client.post("/predict", json=data)

    assert response.status_code == 200

    result = response.json()
    assert "prediction" in result


def test_prediction_invalid():
    data = "invalid"

    response = client.post("/predict", json=data)

    assert response.status_code == 422