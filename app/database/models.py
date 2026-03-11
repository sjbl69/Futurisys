from sqlalchemy import Column, Integer, Float, DateTime
from datetime import datetime
from .db import Base

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    feature1 = Column(Float)
    feature2 = Column(Float)
    prediction = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)