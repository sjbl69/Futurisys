from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_prediction_valid():
    data = [1, 2, 3, 4]
    response = client.post("/predict", json=data)
    assert response.status_code == 200
    assert "prediction" in response.json()


def test_prediction_invalid():
    data = "invalid"
    response = client.post("/predict", json=data)
    assert response.status_code == 422


def test_prediction_wrong_length():
    data = [1, 2]
    response = client.post("/predict", json=data)
    assert response.status_code in [400, 422]