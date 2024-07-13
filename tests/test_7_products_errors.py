from fastapi.testclient import TestClient
from backend.apis.app import app

client = TestClient(app)


def test_invalid_post_products():
    response = client.post("/products", json={"name":"pizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizzapizza","price":10,"stock":10,"category_id":1,"producer_id":3})
    assert response.status_code == 400
    assert response.json() == {"detail":"Name len must be less than 256"}
    
    
def test_invalid_post_products_1():
    response = client.post("/products", json={"name":"","price":10,"stock":10,"category_id":1,"producer_id":3})
    assert response.status_code == 400
    assert response.json() == {"detail":"Name cannot be null"}
    
    
def test_invalid_post_products_2():
    response = client.post("/products", json={"name":"pizza","price":-30,"stock":10,"category_id":1,"producer_id":3})
    assert response.status_code == 400
    assert response.json() == {"detail":"Price must be at least 0"}
    
    
def test_invalid_post_products_3():
    response = client.post("/products", json={"name":"pizza","price":10,"stock":-10,"category_id":1,"producer_id":3})
    assert response.status_code == 400
    assert response.json() == {"detail":"Stock must be at least 0"}
    
    
def test_invalid_post_products_4():
    response = client.post("/products", json={"name":"pizza","price":10,"stock":10,"category_id":0,"producer_id":3})
    assert response.status_code == 400
    assert response.json() == {"detail":"Category_id must be positive"}
    
    
def test_invalid_post_products_5():
    response = client.post("/products", json={"name":"pizza","price":10,"stock":10,"category_id":1,"producer_id":-3})
    assert response.status_code == 400
    assert response.json() == {"detail":"Producer_id must be positive"}
    
    
def test_invalid_post_products_6():
    response = client.post("/products", json={"name":3222,"price":"10","stock":[10,33],"category_id":"1","producer_id":"four"})
    assert response.status_code == 422