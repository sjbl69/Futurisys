from fastapi.testclient import TestClient
from app.main import app
from app.database.db import SessionLocal
from app.database.models import Prediction

client = TestClient(app)


def test_prediction_saved_in_database():
    data = {"features": [1, 2, 3, 4]}

    response = client.post("/predict", json=data)

    assert response.status_code == 200

    db = SessionLocal()

    prediction = db.query(Prediction).order_by(Prediction.id.desc()).first()

    assert prediction is not None
    assert prediction.feature1 == 1
    assert prediction.feature2 == 2
    assert prediction.feature3 == 3
    assert prediction.feature4 == 4

    db.close()