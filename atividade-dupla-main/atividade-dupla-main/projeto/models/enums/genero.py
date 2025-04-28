from enum import Enum

class Genero(Enum):
    MASCULINO = ("Masculino", "M")
    FEMININO = ("Feminino", "F")

    def __init__(self, nome: str, charNome: str) -> None:
        self.nome = nome
        self.charNome = charNome

    def get_nome(self) -> str:
        return self.nome

    def get_charNome(self) -> str:
        return self.charNome
