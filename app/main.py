import os
from fastapi import FastAPI
from app.models.ml_model import predict

app = FastAPI()

APP_ENV = os.getenv("APP_ENV", "development")

@app.get("/")
def read_root():
    return {
        "message": "Futurisys ML API",
        "environment": APP_ENV
    }