from abc import ABC, abstractmethod

from ..models.fisica import PessoaFisica
from ..models.pessoa import DadosPessoa
from ..models.enums.estadoCivil import EstadoCivil
from ..models.enums.genero import Genero
from ..models.enums.setor import Setor

class Funcionario(PessoaFisica ,ABC):
    def __init__(self, sexo: Genero, estadoCivil: EstadoCivil, dataNascimento: str, dadosPessoa: 
                 DadosPessoa, cpf: str, rg: str, matricula: str, setor: Setor, salario: float) -> None:
        super().__init__(sexo, estadoCivil, dataNascimento, dadosPessoa)
        self.CPF = self._verificar_tamanho_CPF(cpf)
        self.RG = self._verificar_tamanho_RG(rg)
        self.matricula = matricula
        self.setor = setor
        self.salario = salario

    def _verificar_tamanho_cpf(self, CPF):
            if len(CPF) > 14:
                raise TypeError("CPF inválido")
            return CPF
        
    def _verificar_tamanho_rg(self, RG):
            if len(RG) > 12:
                raise TypeError("RG inválido")
            return RG
    
    def _verificar_salario(self, salario):
        pass

    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\n\n*== DADOS DO FUNCIONARIO ==*"
            f"\nCPF: {self.cpf}"
            f"\nRG: {self.rg}"
            f"\nMatricula: {self.matricula}"
            f"\nSetor: {self.setor}"
            f"\nSalario: {self.salario}"
        )
