from fastapi.testclient import TestClient
from backend.apis.app import app

client = TestClient(app)


def test_post_products():
    response = client.post("/products", json={"name":"pizza","price":10,"stock":10,"category_id":1,"producer_id":3})
    assert response.status_code == 200
    assert response.json() == {"status":"ok"}
    
    
def test_post_products_1():
    response = client.post("/products", json={"name":"hamburger","price":6,"stock":15,"category_id":1,"producer_id":1})
    assert response.status_code == 200
    assert response.json() == {"status":"ok"}
    
    
def test_get_products():
    response = client.get("/products")
    assert response.status_code == 200
    assert response.json() == [{
        "id": 1,
        "name":"pizza",
        "price":10,
        "stock":10,
        "category_id":1,
        "producer_id":3
    },
    {
        "id": 2,
        "name":"hamburger",
        "price":6,
        "stock":15,
        "category_id":1,
        "producer_id":1
    }]
    
    
def test_put_products():
    response = client.put("/products/1", json={"name":"pizza","price":14,"stock":10,"category_id":1,"producer_id":3})
    assert response.status_code == 200
    assert response.json() == {"status":"ok"}
    
    
def test_delete_products():
    response = client.delete("/products/2")
    assert response.status_code == 200
    assert response.json() == {"status":"ok"}
    
    
def test_get_products_1():
    response = client.get("/products")
    assert response.status_code == 200
    assert response.json() == [{
        "id": 1,
        "name":"pizza",
        "price":14,
        "stock":10,
        "category_id":1,
        "producer_id":3
    }]