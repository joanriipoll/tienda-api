from fastapi.testclient import TestClient

def test_create_e2e(client: TestClient):
    payload = {
        "name": "Mechanical Keyboard", 
        "price": 120.50,
        "stock": 15,
        "category": "Electronics"
    }
    
    response = client.post("/products/", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 1  
    assert data["price"] == 120.50
    assert data["stock"] == 15
    assert data["category"] == "Electronics"


def test_validation_guardrails_e2e(client: TestClient):
    bad_price_payload = {
        "name": "Gaming Mouse", 
        "price": -10.0,
        "stock": 5,
        "category": "Electronics"
    }
    
    response_price = client.post("/products/", json=bad_price_payload)
    assert response_price.status_code == 422
    bad_stock_payload = {
        "name": "Gaming Mouse", 
        "price": 25.0,
        "stock": -5,
        "category": "Electronics"
    }
    
    response_stock = client.post("/products/", json=bad_stock_payload)
    assert response_stock.status_code == 422


def test_read_by_id_e2e(client: TestClient):
    setup_payload = {
        "name": "Monitor", 
        "price": 300.0,
        "stock": 8,
        "category": "Electronics"
    }
    response_create = client.post("/products/", json=setup_payload)
    created_id = response_create.json()["id"]
    response_valid = client.get(f"/products/{created_id}")
    assert response_valid.status_code == 200
    assert response_valid.json()["name"] == "Monitor"
    response_invalid = client.get("/products/999")
    assert response_invalid.status_code == 404


def test_update_and_delete_e2e(client: TestClient):
    initial_payload = {
        "name": "Headphones", 
        "price": 50.0,
        "stock": 20,
        "category": "Audio"
    }
    response_create = client.post("/products/", json=initial_payload)
    created_id = response_create.json()["id"]
    
    update_payload = {
        "name": "Wireless Headphones", 
        "price": 80.0,
        "stock": 12,
        "category": "Audio"
    }
    response_update = client.put(f"/products/{created_id}", json=update_payload)
    assert response_update.status_code == 200
    assert response_update.json()["price"] == 80.0
    assert response_update.json()["stock"] == 12
    response_delete = client.delete(f"/products/{created_id}")
    assert response_delete.status_code in [200, 204] 
    response_verify = client.get(f"/products/{created_id}")
    assert response_verify.status_code == 404