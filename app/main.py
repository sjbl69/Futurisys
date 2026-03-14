import os
from datetime import datetime

from fastapi import FastAPI, Body, HTTPException

from app.models.ml_model import predict
from app.database.db import SessionLocal
from app.database.models import Prediction


app = FastAPI()


@app.get("/")
def read_root():
    return {
        "message": "Futurisys ML API",
        "environment": os.getenv("APP_ENV", "development")
    }


@app.post("/predict")
def get_prediction(features: list = Body(...)):

    if len(features) != 4:
        raise HTTPException(
            status_code=400,
            detail="Exactly 4 features are required"
        )

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