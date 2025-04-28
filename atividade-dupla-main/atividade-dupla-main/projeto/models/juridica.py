from abc import ABC, abstractmethod

from ..models.pessoa import DadosPessoa
from ..models.endereco import Endereco

class PessoaJuridica(DadosPessoa, ABC):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricaoEstadual: str,) -> None:
        super().__init__(id, nome, telefone, email, endereco)
        self.cnpj = self._verificar_tamanho_cnpj(cnpj)
        self.inscricaoEstadual = inscricaoEstadual

    def _verificar_tamanho_cnpj(self, CNPJ):
            if len(CNPJ) > 14:
                raise TypeError("CNPJ inválido.")
            return CNPJ

    def __str__(self) -> str:
         return super().__str__()

    def __str__(self) -> str:
        return (
            f"\nCNPJ: {self.cnpj}"
            f"\nInscrição Estadual: {self.inscricaoEstadual}"
        )
