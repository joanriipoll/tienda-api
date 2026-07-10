from typing import Generator
import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session
from sqlalchemy import text  
from app.main import app
from app.database import engine, get_session

def get_session_override():
    with Session(engine) as session:
        yield session

app.dependency_overrides[get_session] = get_session_override

@pytest.fixture(scope="function")
def client() -> Generator[TestClient, None, None]:
    with Session(engine) as session:
        session.exec(text("TRUNCATE TABLE products RESTART IDENTITY CASCADE;"))
        session.commit()
    
    with TestClient(app) as test_client:
        yield test_client
        