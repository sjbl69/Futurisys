import os
from fastapi import FastAPI
from app.models.ml_model import predict
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()

APP_ENV = os.getenv("APP_ENV", "development")


class PredictionRequest(BaseModel):
    features: List[float] = Field(
        ...,
        min_items=4,
        max_items=4,
        example=[1.0, 2.0, 3.0, 4.0]
    )


@app.get("/")
def read_root():
    return {
        "message": "Futurisys ML API",
        "environment": APP_ENV
    }


@app.post("/predict")
def get_prediction(data: PredictionRequest):
    result = predict(data.features)
    return {"prediction": result}