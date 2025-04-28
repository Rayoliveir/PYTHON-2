import pytest


from ..models.enums.estadoCivil import EstadoCivil
from ..models.enums.genero import Genero
from ..models.enums.setor import Setor
from ..models.enums.unidadeFederativa import UnidadeFederativa
from ..models.advogado import Advogado
from ..models.endereco import Endereco
from ..models.pessoa import DadosPessoa


@pytest.fixture

def validar_advogado():
    advogado = Advogado("OAB", Genero.FEMININO, EstadoCivil.CASADO, "DD/MM/AAAA", DadosPessoa(18, "Nome", "Telefone", "Email", 
                Endereco("Logradouro", "Numero", "Complemento", "Cep", "Cidade", UnidadeFederativa.BAHIA)), 
                "cpf", "rg", "Matricula", Setor.JURIDICO, 7000.0)
    return advogado

#validando atributos
def test_pessoa_id_valido(validar_advogado: Advogado):
    assert validar_advogado.id == 18

def test_pessoa_nome_valido(validar_advogado: Advogado):
    assert validar_advogado.nome == "Nome"

def test_pessoa_telefone_valido(validar_advogado: Advogado):
    assert validar_advogado.telefone == "Telefone"

def test_pessoa_email_valido(validar_advogado: Advogado):
    assert validar_advogado.email == "Email"

def test_cpf_valido(validar_advogado: Advogado):
    assert validar_advogado.cpf == "cpf"

def test_rg_valido(validar_advogado: Advogado):
    assert validar_advogado.rg == "rg"
    
def test_endereco_logradouro_valido(validar_advogado: Advogado):
    assert validar_advogado.endereco.logradouro == "Longradouro"

def test_endereco_numero_valido(validar_advogado: Advogado):
    assert validar_advogado.endereco.numero == "Numero"

def test_endereco_complemento_valido(validar_advogado: Advogado):
    assert validar_advogado.endereco.complemento == "Complemento"

def test_endereco_cep_valido(validar_advogado: Advogado):
    assert validar_advogado.endereco.cep == "Cep"

def test_endereco_cidade_valido(validar_advogado: Advogado):
    assert validar_advogado.endereco.cidade == "Cidade"

def test_endereco_uf_valido(validar_advogado: Advogado):
    assert validar_advogado.endereco.uf == UnidadeFederativa.BAHIA

def test_genero_valido(validar_advogado: Advogado):
    assert validar_advogado.sexo == Genero.MASCULINO

def test_estado_civil_valido(validar_advogado: Advogado):
    assert validar_advogado.estadoCivil == EstadoCivil.CASADO

def test_data_nascimento_valido(validar_advogado: Advogado):
    assert validar_advogado.dataNascimento == "DD/MM/AAAA"



def test_matricula_valido(validar_advogado: Advogado):
    assert validar_advogado.matricula == "Matricula"

def test_setor_valido(validar_advogado: Advogado):
    assert validar_advogado.setor == Setor.JURIDICO

def test_salario_valido(validar_advogado: Advogado):
    assert validar_advogado.salario == 7000.0

def test_oab_valido(validar_advogado: Advogado):
    assert validar_advogado.oab == "OAB"

#testando exceções
def test_id_tipo_errado(validar_advogado: Advogado):
    with pytest.raises(TypeError, match = "valor inválido"):
        Advogado("OAB", Genero.FEMININO, EstadoCivil.CASADO, "DD/MM/AAAA", DadosPessoa("18", "Nome", "Telefone", "Email", 
                Endereco("Logradouro", "Numero", "Complemento", "Cep", "Cidade", 
                UnidadeFederativa.BAHIA)), "cpf", "rg", "Matricula", Setor.JURIDICO, 7000.0)
        
def test_id_valor_negativo(validar_advogado: Advogado):
    with pytest.raises(ValueError, match = "valor inválido"):
       Advogado("OAB", Genero.FEMININO, EstadoCivil.CASADO, "DD/MM/AAAA", DadosPessoa(-18, "Nome", "Telefone", "Email", 
                Endereco("Logradouro", "Numero", "Complemento", "Cep", "Cidade", 
                UnidadeFederativa.BAHIA)), "cpf", "rg", "Matricula", Setor.JURIDICO, 7000.0)

def test_nome_vazio(validar_advogado: Advogado):
    with pytest.raises(ValueError, match = "o nome não pode estar em branco"):
        Advogado("OAB", Genero.FEMININO, EstadoCivil.CASADO, "DD/MM/AAAA", DadosPessoa(18, "", "Telefone", "Email", 
                Endereco("Logradouro", "Numero", "Complemento", "Cep", "Cidade", 
                UnidadeFederativa.BAHIA)), "cpf", "rg", "Matricula", Setor.JURIDICO, 7000.0)

def test_salario_tipo_errado(validar_advogado: Advogado):
    with pytest.raises(TypeError, match = "dado incorreto"):
        Advogado("OAB", Genero.FEMININO, EstadoCivil.CASADO, "DD/MM/AAAA", DadosPessoa(18, "Nome", "Telefone", "Email", 
                Endereco("Logradouro", "Numero", "Complemento", "Cep", "Cidade", 
                UnidadeFederativa.BAHIA)), "cpf", "rg", "Matricula", Setor.JURIDICO, "7000.0")

def test_salario_negativo(validar_advogado: Advogado):
    with pytest.raises(ValueError, match = "salário não pode ser negativo"):
        Advogado("OAB", Genero.FEMININO, EstadoCivil.CASADO, "DD/MM/AAAA", DadosPessoa(18, "Nome", "Telefone", "Email", 
                Endereco("Logradouro", "Numero", "Complemento", "Cep", "Cidade",
                UnidadeFederativa.BAHIA)), "cpf", "rg", "Matricula", Setor.JURIDICO, -7000.0)

def test_cep_invalido(validar_advogado: Advogado):
    with pytest.raises(match = "CEP inválido"):
        Advogado("OAB", Genero.FEMININO, EstadoCivil.CASADO, "DD/MM/AAAA", DadosPessoa(18, "Nome", "Telefone", "Email", 
                Endereco("Logradouro", "Numero", "Complemento", "Cep7", "Cidade", 
                UnidadeFederativa.BAHIA)), "cpf", "rg", "Matricula", Setor.JURIDICO, 7000.0)
        
def test_rg_invalido(validar_advogado: Advogado):
    with pytest.raises( match = "RG inválido"):
        Advogado("OAB", Genero.FEMININO, EstadoCivil.CASADO, "DD/MM/AAAA", DadosPessoa(18, "Nome", "Telefone", "Email", 
                Endereco("Logradouro", "Numero", "Complemento", "Cep", "Cidade", 
                UnidadeFederativa.BAHIA)), "cpf", "rg4", "Matricula", Setor.JURIDICO, 7000.0)
        
def test_cpf_invalido(validar_advogado: Advogado):
    with pytest.raises( match = "CPF inválido"):
        Advogado("OAB", Genero.FEMININO, EstadoCivil.CASADO, "DD/MM/AAAA", DadosPessoa(18, "Nome", "Telefone", "Email", 
                Endereco("Logradouro", "Numero", "Complemento", "Cep", "Cidade", 
                UnidadeFederativa.BAHIA)), "cpf4", "rg", "Matricula", Setor.JURIDICO, 7000.0)