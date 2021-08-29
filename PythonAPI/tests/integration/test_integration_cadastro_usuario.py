import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def create_server_success():
    return [
        {
            "id": None,
            "nome": "SSA - BOMFIM",
            "login": "caio",
            "senha": "210965Vd"
        },
        {
            "id": None,
            "nome": "SSA - CAM DE AREIA",
            "login": "caio",
            "senha": "2109.D"
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
    response = client.post("/servidores", json=server)

    assert response.status_code == 202
    
    
def test_create_server_bad_request():
    server = create_server_bad_request()
    response = client.post("/servidores", json=server)

    assert response.status_code == 400
