from enum import Enum

class Sexo(Enum):
    MASCULINO = ("Masculino", "M")
    FEMININO = ("Feminino", "F")

    def __init__(self, genero, caracter) -> None:
        self.texto = genero
        self.caracter = caracter