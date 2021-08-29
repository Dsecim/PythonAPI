import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def create_server_success():
    return [
        {
            "id": None,
            "nome": "SSA - BOMFIM",
            "url": None,
            "ip": "192.168.88.1",
            "status": "ativo",
            "login": "caio",
            "senha": "210965Vd"
        },
        {
            "id": None,
            "nome": "SSA - CAM DE AREIA",
            "url": "d56a0c23eb70.sn.mynetname.net",
            "ip": "186.210.217.142",
            "status": "ativo",
            "login": "caio",
            "senha": "210965Vd$@lula"
        }
    ]


def test_create_server_success():
    server = create_server_success()
    response = client.post("/servidores", json=server)

    assert response.status_code == 202