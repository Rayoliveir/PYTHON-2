from ..models.juridica import PessoaJuridica
from ..models.endereco import Endereco


class PrestacaoServico(PessoaJuridica):
    def __init__(self, contratoInicio: str, contratoFim: str, id: int, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricaoEstadual: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, cnpj, inscricaoEstadual)
        self.contratoInicio = contratoInicio
        self.contratoFim = contratoFim

    def __str__(self) -> str:
        return super().__str__()
    
    def __str__(self) -> str:
        return (
            f"\nInicio do contrato: {self.contratoInicio}"
            f"\nFim do contrato: {self.contratoFim}"
            )
