from fastapi.testclient import TestClient
from backend.apis.app import app

client = TestClient(app)


def test_post_sales():
    response = client.post("/sales", json={"product_id":1,"total_price":20,"amount":2})
    assert response.status_code == 200
    assert response.json() == {"status":"ok"}
    
    
def test_post_sales_1():
    response = client.post("/sales", json={"product_id":1,"total_price":18,"amount":3})
    assert response.status_code == 200
    assert response.json() == {"status":"ok"}
    
    
def test_get_sales():
    response = client.get("/sales")
    assert response.status_code == 200
    assert len(response.json()) == 2
    
    
def test_delete_sales():
    response = client.delete("/sales/2")
    assert response.status_code == 200
    assert response.json() == {"status":"ok"}
    
    
def test_get_sales_1():
    response = client.get("/sales")
    assert response.status_code == 200
    assert len(response.json()) == 1