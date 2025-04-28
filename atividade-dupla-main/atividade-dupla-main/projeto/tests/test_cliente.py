import pytest


from ..models.enums.estadoCivil import EstadoCivil
from ..models.enums.genero import Genero
from ..models.enums.setor import Setor
from ..models.enums.unidadeFederativa import UnidadeFederativa
from ..models.cliente import Cliente
from ..models.endereco import Endereco
from ..models.pessoa import DadosPessoa


@pytest.fixture
def cliente_valido():
    cliente = Cliente("protocolo Atendimento", Genero.MASCULINO,EstadoCivil.CASADO, "DD/MM/AAAA", DadosPessoa(18, "Nome", "Telefone", "Email", 
        Endereco("Lomgradouro", "Numero", "Complemento", "cep", "Cidade", UnidadeFederativa.BAHIA), "Protocolo Atendimento"))
    return cliente 



#validando atributos
def test_atributo_nome_valido(cliente_valido: Cliente):
    assert cliente_valido.nome == "Nome"

def test_atributo_id_valido(cliente_valido: Cliente):
    assert cliente_valido.id == 18

def test_atributo_telefone_valido(cliente_valido: Cliente):
    assert cliente_valido.telefone == "Telefone"

def test_atributo_email_valido(cliente_valido: Cliente):
    assert cliente_valido.email == "Email"

def test_logradouro_valido(cliente_valido: Cliente):
    assert cliente_valido.endereco.logradouro == "Lomgradouro"

def test_numero_valido(cliente_valido: Cliente):
    assert cliente_valido.endereco.numero == "Numero"

def test_complemento_valido(cliente_valido: Cliente):
    assert cliente_valido.endereco.complemento == "Complemento"

def test_cep_valido(cliente_valido: Cliente):
    assert cliente_valido.endereco.cep == "cep"

def test_cidade_valido(cliente_valido: Cliente):
    assert cliente_valido.endereco.cidade == "Cidade"

def test_uf_valido(cliente_valido: Cliente):
    assert cliente_valido.endereco.uf == UnidadeFederativa.BAHIA

def test_genero_valido(cliente_valido: Cliente):
    assert cliente_valido.genero.sexo == Genero.MASCULINO

def test_estado_civil_valido(cliente_valido: Cliente):
    assert cliente_valido.estadoCivil == EstadoCivil.CASADO

def test_data_nascimento_valido(cliente_valido: Cliente):
    assert cliente_valido.dataNascimento == "DD/MM/AAAA"

def test_protocolo_atendimento_valido(cliente_valido: Cliente):
    assert cliente_valido.protocoloAtendimento == "Protocolo Atendimento"


#testando exceções
def test_id_tipo_errado(cliente_valido: Cliente):
    with pytest.raises(TypeError, match = "valor inválido"):
        Cliente("f", "Nome", "Telefone", "Email",
                    Endereco("Lomgradouro", "Numero", "Complemento", "cep", "Cidade", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "24/09/1999",7777)

def test_id_valor_negativo(cliente_valido: Cliente):
    with pytest.raises(ValueError, match = "valor inválido"):
        Cliente(-18, "Nome", "Telefone", "Email",
                    Endereco("Lomgradouro", "Numero", "Complemento", "cep", "Cidade", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "24/09/1999",7777)

def test_nome_vazio(cliente_valido: Cliente):
    with pytest.raises(ValueError, match = "o nome não pode estar em branco"):
        Cliente(18, "", "Telefone", "Email",
                    Endereco("Lomgradouro", "Numero", "Complemento", "cep", "Cidade", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "24/09/1999",7777)

def test_cep_invalido(cliente_valido: Cliente):
    with pytest.raises(match = "CEP inválido"):
        Cliente(18, "Nome", "Telefone", "Email",
                    Endereco("Lomgradouro", "Numero", "Complemento", "cep7", "Cidade", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "24/09/1999", 7777)
