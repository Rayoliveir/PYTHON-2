from ..models.enums.unidadeFederativa import UnidadeFederativa


class Endereco:
    def __init__(self, longradouro: str, numero: int, complemento: str, cep: str, cidade: str, uf: UnidadeFederativa) -> None:
        self.longradouro = longradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade
        self.uf = uf

    
    def _verificar_tipo_numero_da_casa(self, numero):
            if not isinstance(numero, int):
                raise TypeError("Digite apenas números para o número da casa.")
            if numero < 0:
                raise ValueError("Digite apenas números positivos para o numero da casa")
            return numero
    
    def _verificar_tipo_cep(self, cep):
            if not isinstance(cep, int):
                raise TypeError("Digite apenas números para o cep.")
            if cep < 0:
                raise ValueError("Digite apenas números positivos para o cep")
            return cep
    
    def __str__(self) -> str:
        return (
            f"\nLongradouro: {self.longradouro}"
            f"\nNúmero: {self.numero}"
            f"\nComplemento: {self.complemento}"
            f"\nCnumeroade: {self.numero}"
            f"\nCEP: {self.cep}"
            f"\nUnidade Federativa: {self.uf}"
        )