from ..models.juridica import PessoaJuridica
from ..models.endereco import Endereco


class Fornecedor(PessoaJuridica):
    def __init__(self, nomeProduto: str, id: int, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricaoEstadual: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, cnpj, inscricaoEstadual)
        self.produto = nomeProduto


    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nNome do produto: {self.produto}"
            )
