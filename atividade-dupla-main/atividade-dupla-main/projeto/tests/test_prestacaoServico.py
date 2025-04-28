import pytest
from ..models.endereco import Endereco
from ..models.pessoa import DadosPessoa
from ..models.prestacaoServico import PrestacaoServico
from ..models.enums.unidadeFederativa import UnidadeFederativa

@pytest.fixture
def prestacao_servico_valida():
        return PrestacaoServico("cnpj", "Contrato inicio", "Contrato final", DadosPessoa(18, "Nome", "Telefone", "Email", 
                Endereco("Longradouro", "Numero", "Complemento", "cep", "Cidade", UnidadeFederativa.BAHIA)),"inscriçao estadual")

#validando atributos
def test_id_valido(prestacao_servico_valida: PrestacaoServico):
    assert prestacao_servico_valida.id == 18

def test_nome_valido(prestacao_servico_valida: PrestacaoServico):
    assert prestacao_servico_valida.nome == "Nome"

def test_telefone_valido(prestacao_servico_valida: PrestacaoServico):
    assert prestacao_servico_valida.telefone == "Telefone"

def test_email_valido(prestacao_servico_valida: PrestacaoServico):
    assert prestacao_servico_valida.email == "Email"

def test_logradouro_valido(prestacao_servico_valida: PrestacaoServico):
    assert prestacao_servico_valida.endereco.logradouro == "Longradouro"

def test_numero_valido(prestacao_servico_valida: PrestacaoServico):
    assert prestacao_servico_valida.endereco.numero == "Numero"

def test_complemento_valido(prestacao_servico_valida: PrestacaoServico):
    assert prestacao_servico_valida.endereco.complemento == "Complemento"

def test_cep_valido(prestacao_servico_valida: PrestacaoServico):
    assert prestacao_servico_valida.endereco.cep == "cep"

def test_cidade_valido(prestacao_servico_valida: PrestacaoServico):
    assert prestacao_servico_valida.endereco.cidade == "Cidade"

def test_uf_valido(prestacao_servico_valida: PrestacaoServico):
    assert prestacao_servico_valida.endereco.uf == UnidadeFederativa.BAHIA

def test_cnpj_valido(prestacao_servico_valida: PrestacaoServico):
    assert prestacao_servico_valida.cnpj == "cnpj"

def test_inscricao_estadual_valida(prestacao_servico_valida: PrestacaoServico):
    assert prestacao_servico_valida.inscricaoEstadual == "inscriçao estadual"

def test_inicio_contrato_valido(prestacao_servico_valida: PrestacaoServico):
    assert prestacao_servico_valida.contratoInicio == "01/09/23"

def test_fim_contrato_valido(prestacao_servico_valida: PrestacaoServico):
    assert prestacao_servico_valida.contratoFim == "01/09/24"

#testando exceções
def test_id_tipo_errado(prestacao_servico_valida: PrestacaoServico):
    with pytest.raises(TypeError, match = "valor inválido"):
        PrestacaoServico("f", "Nome", "Telefone", "Email",
                    Endereco("Longradouro", "Numero", "Complemento", "cep", "Cidade", UnidadeFederativa.BAHIA),
                    "cnpj","inscriçao estadual","01/09/23","01/09/24")

def test_id_valor_negativo(prestacao_servico_valida: PrestacaoServico):
    with pytest.raises(ValueError, match = "valor inválido"):
        PrestacaoServico(-18, "Nome", "Telefone", "Email",
                    Endereco("Longradouro", "Numero", "Complemento", "cep", "Cidade", UnidadeFederativa.BAHIA),
                    "cnpj","inscriçao estadual","01/09/23","01/09/24")

def test_nome_vazio(prestacao_servico_valida: PrestacaoServico):
    with pytest.raises(ValueError, match = "o nome não pode estar em branco"):
        PrestacaoServico(18, "", "Telefone", "Email",
                    Endereco("Longradouro", "Numero", "Complemento", "cep", "Cidade", UnidadeFederativa.BAHIA),
                    "cnpj","inscriçao estadual","01/09/23","01/09/24")

def test_cep_invalido(prestacao_servico_valida: PrestacaoServico):
    with pytest.raises(match = "CEP inválido"):
        PrestacaoServico(18, "Nome", "Telefone", "Email",
                    Endereco("Longradouro", "Numero", "Complemento", "cep0", "Cidade", UnidadeFederativa.BAHIA),
                    "cnpj","inscriçao estadual","01/09/23","01/09/24")