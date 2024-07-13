from fastapi.testclient import TestClient
from backend.apis.app import app

client = TestClient(app)


def test_invalid_id():
    response = client.get("/producers/-1")
    assert response.status_code == 400
    assert response.json() == {"detail":"ID must be positive"}
    
    
def test_invalid_id_1():
    response = client.get("/producers/0")
    assert response.status_code == 400
    assert response.json() == {"detail":"ID must be positive"}
    
    
def test_invalid_producer():
    response = client.post("/producers", json={"name" : ["hols","ewww"]})
    assert response.status_code == 422
    
    
def test_invalid_producer_1():
    response = client.post("/producers", json={"name": ""})
    assert response.status_code == 400
    assert response.json() == {"detail":"Name cannot be null"}
    
    
def test_invalid_producer_2():
    response = client.post("/producers", json={"name":"qwertyuiopasdfghjklzxcvbnbmqwertyuiopasdfghjklzxcvbnbmqwertyuiopasdfghjklzxcvbnbmqwertyuiopasdfghjklzxcvbnbmqwertyuiopasdfghjklzxcvbnbmqwertyuiopasdfghjklzxcvbnbmqwertyuiopasdfghjklzxcvbnbmqwertyuiopasdfghjklzxcvbnbmqwertyuiopasdfghjklzxcvbnbmqwertyuiopasdfghjklzxcvbnbm"})
    assert response.status_code == 400
    assert response.json() == {"detail":"Name len must be less than 101"}