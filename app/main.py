from fastapi import FastAPI
from app.models.ml_model import predict

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Futurisys ML API"}

@app.post("/predict")
def get_prediction(features: list):
    result = predict(features)
    return {"prediction": result}