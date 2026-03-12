from app.database.db import SessionLocal
from app.models.db_models import Prediction

db = SessionLocal()

data = [
    Prediction(feature1=1.2, feature2=3.4, feature3=5.6, feature4=7.8, prediction=0.9),
    Prediction(feature1=2.1, feature2=1.5, feature3=4.2, feature4=6.3, prediction=0.4)
]

db.add_all(data)
db.commit()

print("Données insérées")