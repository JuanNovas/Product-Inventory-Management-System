from fastapi.testclient import TestClient
from backend.apis.app import app

client = TestClient(app)


def test_invalid_id():
    response = client.get("/categories/-2")
    assert response.status_code == 400
    assert response.json() == {"detail":"ID must be positive"}
    
    
def test_invalid_id_1():
    response = client.delete("/categories/0")
    assert response.status_code == 400
    assert response.json() == {"detail":"ID must be positive"}
    
    
def test_invalid_category():
    response = client.post("/categories", json={"name":3})
    assert response.status_code == 422
    

def test_invalid_category_1():
    response = client.post("/categories", json={"name":""})
    assert response.status_code == 400
    assert response.json() == {"detail":"Name cannot be null"}
    
    
def test_invalid_category_2():
    response = client.post("/categories", json={"name":"qwertyuiopasdfghjklzxcvbnbmqwertyuiopasdfghjklzxcvbnbmqwertyuiopasdfghjklzxcvbnbmqwertyuiopasdfghjklzxcvbnbmqwertyuiopasdfghjklzxcvbnbmqwertyuiopasdfghjklzxcvbnbmqwertyuiopasdfghjklzxcvbnbmqwertyuiopasdfghjklzxcvbnbmqwertyuiopasdfghjklzxcvbnbmqwertyuiopasdfghjklzxcvbnbm"})
    assert response.status_code == 400
    assert response.json() == {"detail":"Name len must be less than 101"}