from typing import Optional
from domain import commands
from pydantic import (BaseModel, Field, constr, conint)


class UsuarioDTO(BaseModel):
    id: Optional[conint(gt=0,le=9999)] = Field(None,
                                               title='Codigo',
                                               description='Código identificador do servidor')
    nome:  constr(min_length=10) = Field(...,
                                       title='Nome',
                                       description='Nome completo do usuario. Ex:Daniela Secim Netto dos Reys')
    
    login: constr(min_length=6) = Field(...,
                                        title='login',
                                        description='login')
    senha: constr(min_length=7) = Field(...,
                                        title='senha',
                                        description='senha')

    def getCommand(self):
        return commands.Server(
            id=self.id if self.id else None,
            nome=self.nome,
            login=self.login,
            senha=self.senha
        )