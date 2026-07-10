from typing import Generator
import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, create_engine, SQLModel
from sqlalchemy.pool import StaticPool

from app.main import app
from app.database import get_session

TEST_DATABASE_URL = "sqlite://"
engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool, 
)

def get_session_override():
    with Session(engine) as session:
        yield session

app.dependency_overrides[get_session] = get_session_override

@pytest.fixture(scope="function")
def client() -> Generator[TestClient, None, None]:
    # FASE DE SETUP: Borramos cualquier rastro y creamos las tablas limpias
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)
    
    with TestClient(app) as test_client:
        yield test_client