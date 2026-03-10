from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from app.models.ml_model import predict

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

    if len(request.features) != 4:
        raise HTTPException(status_code=422, detail="Invalid number of features")

    result = predict(request.features)

    return {"prediction": result}