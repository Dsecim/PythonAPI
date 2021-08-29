import  pytest 

from pydantic.error_wrappers import ValidationError


def test_inscricao_usuario_valid():
    ServerDTO(
        id= None,
        nome= "SSA - BOMFIM",
        login= "caio",
        senha= "210965Vd"
    )
    
def test_inscricao_usuario_bad_request():
    ServerDTO(
        id= None,
        nome= "12345567890",
        login= "12345567890",
        senha= "12345678910"
    )
    

