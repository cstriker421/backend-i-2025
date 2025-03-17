from fastapi.testclient import TestClient
from src.session_11.exercise_with_challenge.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the FastAPI API!"}

def test_create_item_success():
    response = client.post("/items/", json={"name": "Test Item"})
    assert response.status_code == 200
    assert response.json() == {"item": {"id": 1, "name": "Test Item"}}

def test_create_item_failure():
    response = client.post("/items/", json={"description": "No name provided"})
    assert response.status_code == 400
    assert response.json()["detail"] == "Item must have a name"

def test_update_item_success():

    response = client.post("/items/", json={"name": "Test Item"})
    item_id = response.json()["item"]["id"]  # Extracts the item ID from the response

    updated_item = {"name": "Updated Test Item"}
    response = client.put(f"/items/{item_id}", json=updated_item)
    assert response.status_code == 200
    assert response.json() == {"updated_item": {"id": item_id, "item_id": item_id, "name": "Updated Test Item"}}


def test_update_item_failure():
    
    response = client.put("/items/9999", json={"name": "Non-existent Item"})
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"

def test_delete_item_success():

    response = client.post("/items/", json={"name": "Test Item"})
    item_id = response.json()["item"]["id"]  # Extracts the item ID from the response
    
    response = client.delete(f"/items/{item_id}") # Sends DELETE request to delete the created item
    assert response.status_code == 200
    assert response.json() == {"message": f"Item with ID {item_id} has been deleted"}
    
    response = client.get(f"/items/{item_id}") # Checks that the item no longer exists
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"

def test_delete_item_failure():
    response = client.delete("/items/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"