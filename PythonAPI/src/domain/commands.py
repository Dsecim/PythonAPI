from dataclasses import dataclass
from datetime import date

class Command:
    pass


@dataclass
class Server(Command):
    id: int
    nome: str
    login: str
    senha: str
  
  
@dataclass  
class DeleteServer(Command):
    id: int 
  
    
@dataclass
class Usuario(Command):
    id: int
    nome: str
    login: str
    senha: str