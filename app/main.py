import os
from fastapi import FastAPI, Body
from app.models.ml_model import predict

app = FastAPI()

APP_ENV = os.getenv("APP_ENV", "development")


@app.get("/")
def read_root():
    return {
        "message": "Futurisys ML API",
        "environment": APP_ENV
    }


@app.post("/predict")
def get_prediction(features: list = Body(...)):
    result = predict(features)
    return {"prediction": result}