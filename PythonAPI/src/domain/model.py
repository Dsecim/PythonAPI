from __future__ import annotations


class Server:
    def __init__(self, id: str, descricao: str, url: str, login: str, senha: str):
        self.id = id
        self.descricao = descricao
        self.url = url
        self.login = login
        self.senha = senha