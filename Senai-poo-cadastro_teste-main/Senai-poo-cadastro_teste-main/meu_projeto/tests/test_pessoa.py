import pytest

from meu_projeto.models.endereco import Endereco
from meu_projeto.models.enums.estado import Estado
from meu_projeto.models.enums.sexo import Sexo
from meu_projeto.models.pessoa import Pessoa

# Modelo
@pytest.fixture
def criar_pessoa():
    pessoa_1 = Pessoa(1525, "Joana", 22, "7199999-9999", "joana@gmail.com", Sexo.FEMININO, 
                  Endereco("Rua dinamarca", "250", "Centro", "48900-600", "Xique-xique", Estado.BAHIA))

    return pessoa_1

def test_pessoa_valido(criar_pessoa):
    assert criar_pessoa.nome == "Joana"

def test_pessoa_atributo_idade(criar_pessoa):
    assert criar_pessoa.idade == 22

def test_endereco_longradouro_pessoa(criar_pessoa):
    assert criar_pessoa.endereco.longradouro == "Rua dinamarca"