from __future__ import annotations


class Server:
    def __init__(self, id: str,nome: str, login: str, senha: str):
        self.id = id
        self.nome = nome
        self.login = login
        self.senha = senha