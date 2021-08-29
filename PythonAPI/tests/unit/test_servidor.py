import pytest
from src.domain.dto.server import ServerDTO
from pydantic.error_wrappers import ValidationError


def test_product_valid():
    ServerDTO(
        id= None,
        nome= "SSA - BOMFIM",
        url= None,
        ip= "192.168.88.1",
        status= "ativo",
        login= "caio",
        senha= "210965Vd"
    )