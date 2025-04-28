import pytest

from ..models.endereco import Endereco
from ..models.fornecedor import Fornecedor
from ..models.enums.unidadeFederativa import UnidadeFederativa
from ..models.pessoa import DadosPessoa




@pytest.fixture
def fornecedor_valido():
        fornecedor = Fornecedor("Hardware", "cnpj", "Inscrição estadual", DadosPessoa(18, "Nome", "Telefone", "Email",
                    Endereco("Longradouro", "Numero", "Complemento", "Cep", "Cidade", UnidadeFederativa.BAHIA)))
        return fornecedor

#validando atributos
def test_id_valido(fornecedor_valido: Fornecedor):
    assert fornecedor_valido.id == 18

def test_nome_valido(fornecedor_valido: Fornecedor):
    assert fornecedor_valido.nome == "Nome"

def test_telefone_valido(fornecedor_valido: Fornecedor):
    assert fornecedor_valido.telefone == "Telefone"

def test_email_valido(fornecedor_valido: Fornecedor):
    assert fornecedor_valido.email == "Email"

def test_logradouro_valido(fornecedor_valido: Fornecedor):
    assert fornecedor_valido.endereco.longradouro == "Longradouro"

def test_numero_valido(fornecedor_valido: Fornecedor):
    assert fornecedor_valido.endereco.numero == "Numero"

def test_complemento_valido(fornecedor_valido: Fornecedor):
    assert fornecedor_valido.endereco.complemento == "Complemento"

def test_cep_valido(fornecedor_valido: Fornecedor):
    assert fornecedor_valido.endereco.cep == "Cep"

def test_cidade_valido(fornecedor_valido: Fornecedor):
    assert fornecedor_valido.endereco.cidade == "Cidade"

def test_uf_valido(fornecedor_valido: Fornecedor):
    assert fornecedor_valido.endereco.uf == UnidadeFederativa.BAHIA

def test_cnpj_valido(fornecedor_valido: Fornecedor):
    assert fornecedor_valido.cnpj == "cnpj"

def test_inscricao_estadual_valida(fornecedor_valido: Fornecedor):
    assert fornecedor_valido.inscricaoEstadual == "Inscrição estadual"

#testando exceções
def test_id_tipo_errado(fornecedor_valido: Fornecedor):
    with pytest.raises(TypeError, match = "valor inválido"):
        Fornecedor("Hardware", "cnpj", "Inscrição estadual", DadosPessoa("18", "Nome", "Telefone", "Email",
                    Endereco("Longradouro", "Numero", "Complemento", "Cep", "Cidade", UnidadeFederativa.BAHIA)))

def test_id_valor_negativo(fornecedor_valido: Fornecedor):
    with pytest.raises(ValueError, match = "valor inválido"):
        Fornecedor("Hardware", "cnpj", "Inscrição estadual", DadosPessoa(-18, "Nome", "Telefone", "Email",
                    Endereco("Longradouro", "Numero", "Complemento", "Cep", "Cidade", UnidadeFederativa.BAHIA)))
        
def test_nome_vazio(fornecedor_valido: Fornecedor):
    with pytest.raises(ValueError, match = "o nome não pode estar em branco"):
        Fornecedor("Hardware", "cnpj", "Inscrição estadual", DadosPessoa(18, "", "Telefone", "Email",
                    Endereco("Longradouro", "Numero", "Complemento", "Cep", "Cidade", UnidadeFederativa.BAHIA)))
        
def test_cep_invalido(fornecedor_valido: Fornecedor):
    with pytest.raises(match = "CEP inválido"):
        Fornecedor("Hardware", "cnpj", "Inscrição estadual", DadosPessoa(18, "Nome", "Telefone", "Email",
                    Endereco("Longradouro", "Numero", "Complemento", 54875, "Cidade", UnidadeFederativa.BAHIA)))