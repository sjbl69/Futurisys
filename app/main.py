from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from datetime import datetime

from app.models.ml_model import predict
from app.database.db import SessionLocal
from app.database.models import Prediction

app = FastAPI()


class PredictionRequest(BaseModel):
    features: List[float]


@app.get("/")
def read_root():
    return {
        "message": "Futurisys ML API",
        "environment": "development"
    }


@app.post("/predict")
def get_prediction(request: PredictionRequest):

    features = request.features

    result = predict(features)

    db = SessionLocal()

    prediction_row = Prediction(
        feature1=features[0],
        feature2=features[1],
        feature3=features[2],
        feature4=features[3],
        prediction=result,
        created_at=datetime.utcnow()
    )

    db.add(prediction_row)
    db.commit()
    db.close()

    return {"prediction": result}