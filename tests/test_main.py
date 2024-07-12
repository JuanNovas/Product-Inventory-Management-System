from fastapi.testclient import TestClient
from backend.apis.app import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_read_item_negative_id():
    response = client.get("/products/-1")
    assert response.status_code == 400
    assert response.json() == {"detail": "ID must be positive"}