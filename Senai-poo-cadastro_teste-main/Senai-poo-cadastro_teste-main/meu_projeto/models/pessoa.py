from meu_projeto.models.endereco import Endereco
from meu_projeto.models.enums.sexo import Sexo


class Pessoa:
    def __init__(self, id: int, nome: str, idade: int, telefone: str, email: str, sexo: Sexo, endereco: Endereco) -> None:
        self.id = id
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.email = email
        self.sexo = sexo
        self.endereco = endereco

    def __str__(self) -> str:
        return (
            "*== DADOS DA PESSOA ==*"
            f"\nNome: {self.nome}"
            f"\nIdade: {self.idade}"
            f"\nTelefone: {self.telefone}"
            f"\nE-mail: {self.email}"
            f"\nSexo: {self.sexo.texto} "
            f"\nSexo: {self.sexo.caracter}"
            f"\n\n-- ENDEREÇO -- {self.endereco}\n"
            )
    