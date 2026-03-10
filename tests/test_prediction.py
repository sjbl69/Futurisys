from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_prediction_valid():
    data = {
        "features": [1.0, 2.0, 3.0, 4.0]
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
        "features": [1.0, 2.0]
    }

    response = client.post("/predict", json=data)

    assert response.status_code == 422