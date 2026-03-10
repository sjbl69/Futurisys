from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_prediction_valid():
    data = [1, 2, 3, 4]

    response = client.post("/predict", json=data)

    assert response.status_code == 200


def test_prediction_invalid():
    data = "invalid"

    response = client.post("/predict", json=data)

    assert response.status_code == 422