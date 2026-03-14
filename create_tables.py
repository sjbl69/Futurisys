from app.database.db import engine, Base
from app.database import models

def create_tables():
    print("Création des tables...")
    Base.metadata.create_all(bind=engine)
    print("Tables créées avec succès")

if __name__ == "__main__":
    create_tables()