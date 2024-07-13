from fastapi.testclient import TestClient
from backend.apis.app import app

client = TestClient(app)


def test_get_categories():
    response = client.get("/categories")
    assert response.status_code == 200
    assert response.json() == [{
        "id": 1,
        "name": "food"
    },
    {
        "id": 2,
        "name": "clothes"
    }
    ]
    
    
def test_get_categories_by_id():
    response = client.get("/categories/2")
    assert response.status_code == 200
    assert response.json() == {
        "id" : 2,
        "name" : "clothes"
    }
    
    
def test_post_categories_2():
    response = client.post("/categories", json={"name": "backpacks"})
    assert response.status_code == 200
    assert response.json() == {"status":"ok"}
    
    
def test_get_categories_by_id_1():
    response = client.get("/categories/3")
    assert response.status_code == 200
    assert response.json() == {
        "id" : 3,
        "name" : "backpacks"
    }
    
    
def test_delete_category():
    response = client.delete("/categories/2")
    assert response.status_code == 200
    assert response.json() == {"status":"ok"}
    
    
def test_get_categories_1():
    response = client.get("/categories")
    print(response.json())
    assert response.status_code == 200
    assert response.json() == [{
        "id": 1,
        "name": "food"
    },
    {
        "id" : 3,
        "name" : "backpacks"
    }
    ]
    
    
def test_put_categories():
    response = client.put("/categories/3", json={"name": "keyboards"})
    assert response.status_code == 200
    assert response.json() == {"status":"ok"}
    
    
def test_get_categories_2():
    response = client.get("/categories")
    assert response.status_code == 200
    assert response.json() == [{
        "id": 1,
        "name": "food"
    },
    {
        "id" : 3,
        "name" : "keyboards"
    }
    ]
    
    
def test_post_categories_3():
    response = client.post("/categories", json={"name":"1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"})
    assert response.status_code == 200
    assert response.json() == {"status" : "ok"}