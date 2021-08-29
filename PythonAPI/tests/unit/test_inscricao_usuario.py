import  pytest 
from src.domain.dto.usuario import UsuarioDTO
from pydantic.error_wrappers import ValidationError


def test_inscricao_usuario_valid():
    UsuarioDTO(
        id= None,
        nome= "Daniela",
        login= "dkreys",
        senha= "1234567"
    )
    
def test_inscricao_usuario_bad_request():
    UsuarioDTO(
        id= None,
        nome= "12345567890",
        login= "12345567890",
        senha= "12345678910"
    )
    

