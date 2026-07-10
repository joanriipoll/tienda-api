import os
from sqlmodel import create_engine, Session

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("⚠️ La variable de entorno DATABASE_URL no está configurada.")

engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session