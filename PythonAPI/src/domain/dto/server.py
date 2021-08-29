from typing import Optional
from domain import commands
from pydantic import (BaseModel, Field, constr, conint)


class ServerDTO(BaseModel):
    id: Optional[conint(gt=0,le=9999)] = Field(None,
                                               title='Codigo',
                                               description='Código identificador do servidor')
    nome: constr(min_length=10) = Field(None,
                                       title='Nome',
                                       description='Nome completo do usuario. Ex:Daniela Secim Netto dos Reys')
    
    login: constr(min_length=6) = Field(None,
                                        title='login',
                                        description='login')
    senha: constr(min_length=7) = Field(None,
                                        title='Número do telefone',
                                        description='Número do telefone')

    def getCommand(self):
        return commands.Server(
            id=self.id if self.id else None,
            nome=self.nome if self.nome else None,
            login=self.login if self.login else None,
            senha=self.senha if self.senha else None
        )