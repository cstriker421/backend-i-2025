import pytest
from fastapi.testclient import Testclient
from fastapi import status
from session_13.main import api

@pytest.ficxture(scope="session")
def client():
    return Testclient(api)

def test_api_create_task(client):
    response = client.post("/task")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() is not None