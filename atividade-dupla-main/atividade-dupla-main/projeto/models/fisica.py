from abc import ABC, abstractmethod

from ..models.pessoa import DadosPessoa
from ..models.endereco import Endereco
from ..models.enums.estadoCivil import EstadoCivil
from ..models.enums.genero import Genero

class PessoaFisica(DadosPessoa, ABC):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, sexo: 
        Genero, estadoCivil: EstadoCivil, dataNascimento: str) -> None:
        super().__init__(id, nome, telefone, email, endereco)
        self.sexo = sexo
        self.estadoCivil = estadoCivil
        self.dataNascimento = dataNascimento
        
    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nSexo: {self.sexo}"
            f"\nEstado civil: {self.estadoCivil}"
            f"\nData de nascimento: {self.dataNascimento}"
        )
