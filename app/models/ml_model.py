import joblib

model = joblib.load("ml_model/model.pkl")

def predict(data):
    prediction = model.predict([data])
    return int(prediction[0])