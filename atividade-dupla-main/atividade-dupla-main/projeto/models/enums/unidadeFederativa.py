from enum import Enum

class UnidadeFederativa(Enum):
    BAHIA = ("Bahia", "BA")
    SAO_PAULO = ("São Paulo", "RJ")
    RIO_DE_JANEIRO = ("Rio de Janeiro", "SP")

    def __init__(self, nome: str, sigla: str) -> None:
        self.nome = nome
        self.sigla = sigla

    def get_nome(self) -> str:
        return self.nome

    def get_sigla(self) -> str:
        return self.nome
