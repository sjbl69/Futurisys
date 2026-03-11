import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

from app.models.ml_model import predict
from app.database.db import SessionLocal, engine
from app.database.models import Base, Prediction


app = FastAPI()

# création automatique des tables (important pour CI/tests)
Base.metadata.create_all(bind=engine)

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

    # validation du nombre de features
    if len(data.features) != 4:
        raise HTTPException(
            status_code=422,
            detail="Model expects 4 features"
        )

    # appel du modèle
    result = predict(data.features)

    # transformer array -> float
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