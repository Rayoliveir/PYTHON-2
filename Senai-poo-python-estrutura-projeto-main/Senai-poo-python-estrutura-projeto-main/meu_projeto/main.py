import os
from models.endereco import Endereco
from models.enums.sexo import Sexo
from models.pessoa import Pessoa

os.system("cls || clear")

# Instanciando classe.
pessoa_1 = Pessoa("João", 21, Sexo.MASCULINO, Endereco("R. Dinamarca", "250"))

print(pessoa_1)