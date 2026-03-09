from fastapi import FastAPI, Body
from app.models.ml_model import predict

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Futurisys ML API"}

@app.post("/predict")
def get_prediction(features: list = Body(...)):
    result = predict(features)
    return {"prediction": result}