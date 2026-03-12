from app.database.db import SessionLocal
from app.models.db_models import Prediction

db = SessionLocal()

results = db.query(Prediction).all()

for r in results:
    print(r.id, r.feature1, r.feature2, r.feature3, r.feature4, r.prediction)