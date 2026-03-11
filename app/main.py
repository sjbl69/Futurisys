import os
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from app.models.ml_model import predict
from app.database.db import SessionLocal
from app.database.models import Prediction


app = FastAPI()

APP_ENV = os.getenv("APP_ENV", "development")


class PredictionRequest(BaseModel):
    features: List[float]


@app.get("/")
def read_root():
    return {
        "message": "Futurisys ML API",
        "environment": APP_ENV
    }


@app.post("/predict")
def get_prediction(data: PredictionRequest):

    # appel du modèle
    result = predict(data.features)

    # transformer array -> valeur
    result = float(result[0])

    db = SessionLocal()

    new_prediction = Prediction(
        feature1=data.features[0],
        feature2=data.features[1],
        prediction=result
    )

    db.add(new_prediction)
    db.commit()
    db.close()

    return {"prediction": result}


@app.get("/predictions")
def get_predictions():

    db = SessionLocal()
    predictions = db.query(Prediction).all()
    db.close()

    return predictions