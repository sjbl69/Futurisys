from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from datetime import datetime

from app.models.ml_model import predict
from app.database.db import SessionLocal
from app.database.models import Prediction

app = FastAPI()


# Modèle d'entrée pour l'API
class PredictionRequest(BaseModel):
    features: List[float]


@app.get("/")
def read_root():
    return {"message": "Futurisys ML API"}


@app.post("/predict")
def get_prediction(data: PredictionRequest):

    features = data.features

    result = predict(features)

    db = SessionLocal()

    new_prediction = Prediction(
        feature1=features[0],
        feature2=features[1],
        feature3=features[2],
        feature4=features[3],
        prediction=result,
        created_at=datetime.utcnow()
    )

    db.add(new_prediction)
    db.commit()
    db.close()

    return {"prediction": result}