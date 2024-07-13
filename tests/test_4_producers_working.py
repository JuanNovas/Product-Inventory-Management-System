from fastapi.testclient import TestClient
from backend.apis.app import app

client = TestClient(app)


def test_get_producers():
    response = client.get("/producers")
    assert response.status_code == 200
    assert response.json() == [{
        "id": 1,
        "name": "ABC"
    },
    {
        "id": 2,
        "name": "123"
    }
    ]
    
    
def test_get_producers_by_id():
    response = client.get("/producers/2")
    assert response.status_code == 200
    assert response.json() == {
        "id" : 2,
        "name" : "123"
    }
    
    
def test_post_producers():
    response = client.post("/producers", json={"name": "XYZ"})
    assert response.status_code == 200
    assert response.json() == {"status":"ok"}
    
    
def test_get_producers_by_id_1():
    response = client.get("/producers/3")
    assert response.status_code == 200
    assert response.json() == {
        "id" : 3,
        "name" : "XYZ"
    }
    
    
def test_delete_producers():
    response = client.delete("/producers/2")
    assert response.status_code == 200
    assert response.json() == {"status":"ok"}
    
    
def test_get_producers_1():
    response = client.get("/producers")
    assert response.status_code == 200
    assert response.json() == [{
        "id": 1,
        "name": "ABC"
    },
    {
        "id": 3,
        "name": "XYZ"
    }
    ]
    
    
def test_put_producers():
    response = client.put("/producers/3", json={"name": "890"})
    assert response.status_code == 200
    assert response.json() == {"status":"ok"}
    

def test_get_producers_2():
    response = client.get("/producers")
    assert response.status_code == 200
    assert response.json() == [{
        "id": 1,
        "name": "ABC"
    },
    {
        "id": 3,
        "name": "890"
    }]