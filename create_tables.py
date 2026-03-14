from app.database.db import engine, Base
from app.database.models import Prediction


print("Création des tables...")

Base.metadata.create_all(bind=engine)

print("Tables créées avec succès")