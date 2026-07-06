from typing import Generator
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import INVENTORY

@pytest.fixture(scope="function")
def client() -> Generator[TestClient, None, None]:
    with TestClient(app) as test_client:
        yield test_client
    INVENTORY.clear()