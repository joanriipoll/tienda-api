from typing import Generator
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import INVENTORY, PRODUCT_ID_COUNTER

@pytest.fixture(scope="function")
def client() -> Generator[TestClient, None, None]:
    global PRODUCT_ID_COUNTER
    with TestClient(app) as test_client:
        yield test_client
    INVENTORY.clear()
    PRODUCT_ID_COUNTER = 1