from fastapi.testclient import TestClient
from backend.apis.app import app

client = TestClient(app)


def test_invalid_post_sales():
    response = client.post("/sales", json={"product_id":-1,"total_price":20,"amount":2})
    assert response.status_code == 400
    assert response.json() == {"detail":"Product_id must be positive"}
    
    
def test_invalid_post_sales_1():
    response = client.post("/sales", json={"product_id":0,"total_price":20,"amount":2})
    assert response.status_code == 400
    assert response.json() == {"detail":"Product_id must be positive"}
    
    
def test_invalid_post_sales_2():
    response = client.post("/sales", json={"product_id":1,"total_price":-10,"amount":2})
    assert response.status_code == 400
    assert response.json() == {"detail":"Total price must be at least 0"}
    
    
def test_invalid_post_sales_3():
    response = client.post("/sales", json={"product_id":1,"total_price":10,"amount":0})
    assert response.status_code == 400
    assert response.json() == {"detail":"Amount must be at least 1"}