from ..models.funcionario import Funcionario
from ..models.pessoa import DadosPessoa
from ..models.enums.estadoCivil import EstadoCivil
from ..models.enums.genero import Genero
from ..models.enums.setor import Setor


class Engenheiro(Funcionario):
    def __init__(self, crea: str, sexo: Genero, estadoCivil: 
        EstadoCivil, dataNascimento: str, dadosPessoa: DadosPessoa, cpf: str, rg: str, matricula: str, setor: Setor, salario: float) -> None:
        super().__init__(sexo, estadoCivil, dataNascimento, dadosPessoa, cpf, rg, matricula, setor, salario)
        self.crea = crea

  
    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nCREA: {self.crea}"
            )
