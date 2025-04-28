from ..models.endereco import Endereco
from ..models.pessoa import DadosPessoa


class Cliente(DadosPessoa):
    def __init__(self, protocoloAtendimento: str, id: int, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        super().__init__(id, nome, telefone, email, endereco)
        self.protocoloAtendimento = protocoloAtendimento

    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nNúmero de protocolo: {self.protocoloAtendimento}"
            )
