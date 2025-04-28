from abc import ABC, abstractmethod

from ..models.endereco import Endereco



class DadosPessoa(ABC):
    def __init__(self, id: int, nome: str, telefone: str,  email: str, endereco: Endereco) -> None:
        self.id = self._verificar_tipo_id(id)
        self.nome = self._verificar_nome_vazio(nome)
        self.telefone = self._verificar_tipo_telefone(telefone)
        self.email = self._verificar_email_vazio(email)
        self.endereco = endereco 

    def _verificar_tipo_id(self, id):
            if not isinstance(id, int):
                raise TypeError("Digite apenas números para o ID")
            if id < 0:
                raise ValueError("Digite apenas números positivos para o ID")
            return id

    def _verificar_nome_vazio(self, nome):
            if not isinstance(nome, str) or not nome.strip():
                raise ValueError("O nome não pode estar em branco")
            return nome
    
    def _verificar_tipo_telefone(self, telefone):
        if not isinstance (telefone, str):
            raise TypeError("Digite apenas números.")
        return telefone
    
    def _verificar_email_vazio(self, email):
            if not isinstance(email, str) or not email.strip():
                raise TypeError("Email não pode estar vazio.")
            return email

    def __str__(self) -> str:
        return (
            f"\n*== DADOS PESSOA ==*"
            f"\nD: {self.id}"
            f"\nNome: {self.nome}"
            f"\nTelefone: {self.telefone}"
            f"\nE-mail: {self.email}"
            f"\n\n-- ENDEREÇO --: {self.endereco}"
        )
