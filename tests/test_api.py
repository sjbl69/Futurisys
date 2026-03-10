from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "Futurisys ML API"
    assert "environment" in data


def test_prediction_valid():
    data = {
        "features": [1, 2, 3, 4]
    }

    response = client.post("/predict", json=data)

    assert response.status_code == 200
    assert "prediction" in response.json()


def test_prediction_invalid():
    data = {
        "features": "invalid"
    }

    response = client.post("/predict", json=data)

    assert response.status_code == 422


def test_prediction_wrong_number_features():
    data = {
        "features": [1, 2]
    }

    response = client.post("/predict", json=data)

    assert response.status_code == 422