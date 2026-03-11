import joblib
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "ml_model", "model.pkl")

model = joblib.load(MODEL_PATH)

def predict(features):
    features = np.array(features).reshape(1, -1)
    prediction = model.predict(features)
    return prediction