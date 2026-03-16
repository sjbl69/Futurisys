from sqlalchemy import inspect
from app.database.db import engine
from app.database.models import Base


def test_create_tables():
    Base.metadata.create_all(bind=engine)

    inspector = inspect(engine)
    tables = inspector.get_table_names()

    assert "predictions" in tables