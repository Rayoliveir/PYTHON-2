class Endereco:
    def __init__(self, longradouro: str, numero: str) -> None:
        self.longradouro = longradouro
        self.numero = numero

    def __str__(self) -> str:
        return (
            f"\nLongradouro: {self.longradouro}"
            f"\nNúmero: {self.numero}"
        )
