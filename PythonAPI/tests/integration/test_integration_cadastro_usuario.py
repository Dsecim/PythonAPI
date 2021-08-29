import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def create_server_success():
    return [
        {
            "id": None,
            "nome": "Daniela",
            "login": "dkreys",
            "senha": "1234567"
        },
        {
            "id": None,
            "nome": "Carlos",
            "login": "carossi",
            "senha": "1234567"
        }
    ]
    
def create_server_bad_request():
    return [
        {
            "id": None,
            "nome": "12345567890",
            "login": "12345567890",
            "senha": "12345678910"
        }
    ]


def test_create_server_success():
    server = create_server_success()
    response = client.post("/usuario", json=server)

    assert response.status_code == 202
    
    
def test_create_server_bad_request():
    server = create_server_bad_request()
    response = client.post("/usuario", json=server)

    assert response.status_code == 400
