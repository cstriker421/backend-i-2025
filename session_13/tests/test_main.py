import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel, create_engine, Session
from src.session_13.exercise_with_challenge.main import app, get_session

# Uses SQLite for isolated testing
TEST_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})

@pytest.fixture(name="session")
def session_fixture():
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session
    SQLModel.metadata.drop_all(engine)

@pytest.fixture(name="client")
def client_fixture(session):
    def get_test_session():
        yield session
    app.dependency_overrides[get_session] = get_test_session
    return TestClient(app)

def test_create_item(client):
    response = client.post("/items/", json={"id": 1, "name": "Item 1", "description": "Test item"})
    assert response.status_code == 200
    assert response.json()["name"] == "Item 1"

def test_read_item(client):
    client.post("/items/", json={"id": 2, "name": "Read Test", "description": "For reading"})
    response = client.get("/items/2")
    assert response.status_code == 200
    assert response.json()["name"] == "Read Test"

def test_update_item(client):
    client.post("/items/", json={"id": 3, "name": "Old Name", "description": "Old Desc"})
    response = client.put("/items/3", json={"id": 3, "name": "New Name", "description": "New Desc"})
    assert response.status_code == 200
    assert response.json()["name"] == "New Name"

def test_delete_item(client):
    client.post("/items/", json={"id": 4, "name": "To Delete", "description": "Delete me"})
    response = client.delete("/items/4")
    assert response.status_code == 200
    assert "deleted successfully" in response.json()["message"]

def test_search_items(client):
    client.post("/items/", json={"id": 5, "name": "TestSearch", "description": "desc"})
    response = client.get("/items/search/?query=Search")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["name"] == "TestSearch"

def test_delete_by_keyword(client):
    client.post("/items/", json={"id": 6, "name": "ToDelete1", "description": "delete this"})
    client.post("/items/", json={"id": 7, "name": "ToDelete2", "description": "delete this too"})
    response = client.delete("/items/delete-by-keyword/?keyword=delete")
    assert response.status_code == 200
    assert response.json()["deleted"] == 2
