import pytest


from ..models.endereco import Endereco
from ..models.engenheiro import Engenheiro
from ..models.enums.estadoCivil import EstadoCivil
from ..models.enums.genero import Genero
from ..models.enums.setor import Setor
from ..models.enums.unidadeFederativa import UnidadeFederativa
from ..models.pessoa import DadosPessoa


@pytest.fixture
def engenheiro_valido():
    return Engenheiro("Crea", Genero.MASCULINO, EstadoCivil.CASADO, "DD/MM/AAAA", DadosPessoa(18, "Nome", "Telefone", "Email", 
            Endereco("Longradouro", "Numero", "Complemento", "cep", "Cidade", UnidadeFederativa.BAHIA)), "cpf", "rg", "Matricula", 
            Setor.ENGENHARIA, 7000.0)

#validando atributos

def test_id_valido(engenheiro_valido: Engenheiro):
    assert engenheiro_valido.id == 18

def test_nome_valido(engenheiro_valido: Engenheiro):
    assert engenheiro_valido.nome == "Nome"

def test_telefone_valido(engenheiro_valido: Engenheiro):
    assert engenheiro_valido.telefone == "Telefone"

def test_email_valido(engenheiro_valido: Engenheiro):
    assert engenheiro_valido.email == "Email"

def test_logradouro_valido(engenheiro_valido: Engenheiro):
    assert engenheiro_valido.endereco.longradouro == "Longradouro"

def test_numero_valido(engenheiro_valido: Engenheiro):
    assert engenheiro_valido.endereco.numero == "Numero"

def test_complemento_valido(engenheiro_valido: Engenheiro):
    assert engenheiro_valido.endereco.complemento == "Complemento"

def test_cep_valido(engenheiro_valido: Engenheiro):
    assert engenheiro_valido.endereco.cep == "cep"

def test_cidade_valido(engenheiro_valido: Engenheiro):
    assert engenheiro_valido.endereco.cidade == "Cidade"

def test_uf_valido(engenheiro_valido: Engenheiro):
    assert engenheiro_valido.endereco.uf == UnidadeFederativa.BAHIA

def test_genero_valido(engenheiro_valido: Engenheiro):
    assert engenheiro_valido.sexo == Genero.MASCULINO

def test_estado_civil_valido(engenheiro_valido: Engenheiro):
    assert engenheiro_valido.estadoCivil == EstadoCivil.CASADO

def test_data_nascimento_valido(engenheiro_valido: Engenheiro):
    assert engenheiro_valido.dataNascimento == "DD/MM/AAAA"

def test_cpf_valido(engenheiro_valido: Engenheiro):
    assert engenheiro_valido.cpf == "cpf"

def test_rg_valido(engenheiro_valido: Engenheiro):
    assert engenheiro_valido.rg == "rg"

def test_matricula_valido(engenheiro_valido: Engenheiro):
    assert engenheiro_valido.matricula == "Matricula"

def test_setor_valido(engenheiro_valido: Engenheiro):
    assert engenheiro_valido.setor == Setor.ENGENHARIA

def test_crea_valido(engenheiro_valido: Engenheiro):
    assert engenheiro_valido.crea == "Crea"

def test_salario(engenheiro_valido: Engenheiro):
    assert engenheiro_valido.salario == 7000.0

#testando exceções
# def test_id_tipo_errado(engenheiro_valido: Engenheiro):
#     with pytest.raises(TypeError, match = "valor inválido"):
#        Engenheiro("Crea", Genero.MASCULINO, EstadoCivil.CASADO, "DD/MM/AAAA", DadosPessoa("18", "Nome", "Telefone", "Email", 
#             Endereco("Longradouro", "Numero", "Complemento", "cep", "Cidade", UnidadeFederativa.BAHIA)), "cpf", "rg", "Matricula", 
#             Setor.ENGENHARIA, 7000.0)

# def test_id_valor_negativo(engenheiro_valido: Engenheiro):
#     with pytest.raises(ValueError, match = "valor inválido"):
#         Engenheiro("Crea", Genero.MASCULINO, EstadoCivil.CASADO, "DD/MM/AAAA", DadosPessoa(-18, "Nome", "Telefone", "Email", 
#             Endereco("Longradouro", "Numero", "Complemento", "cep", "Cidade", UnidadeFederativa.BAHIA)), "cpf", "rg", "Matricula", 
#             Setor.ENGENHARIA, 7000.0)
        
# def test_nome_vazio(engenheiro_valido: Engenheiro):
#     with pytest.raises(ValueError, match = "o nome não pode estar em branco"):
#        Engenheiro("Crea", Genero.MASCULINO, EstadoCivil.CASADO, "DD/MM/AAAA", DadosPessoa(18, "", "Telefone", "Email", 
#             Endereco("Longradouro", "Numero", "Complemento", "cep", "Cidade", UnidadeFederativa.BAHIA)), "cpf", "rg", "Matricula", 
#             Setor.ENGENHARIA, 7000.0)
       
# def test_salario_tipo_errado(engenheiro_valido: Engenheiro):
#     with pytest.raises(TypeError, match = "dado incorreto"):
#        Engenheiro("Crea", Genero.MASCULINO, EstadoCivil.CASADO, "DD/MM/AAAA", DadosPessoa(18, "Nome", "Telefone", "Email", 
#             Endereco("Longradouro", "Numero", "Complemento", "cep", "Cidade", UnidadeFederativa.BAHIA)), "cpf", "rg", "Matricula", 
#             Setor.ENGENHARIA, "7000.0")

# def test_salario_negativo(engenheiro_valido: Engenheiro):
#     with pytest.raises(ValueError, match = "salário não pode ser negativo"):
#         Engenheiro("Crea", Genero.MASCULINO, EstadoCivil.CASADO, "DD/MM/AAAA", DadosPessoa(18, "Nome", "Telefone", "Email", 
#             Endereco("Longradouro", "Numero", "Complemento", "cep", "Cidade", UnidadeFederativa.BAHIA)), "cpf", "rg", "Matricula", 
#             Setor.ENGENHARIA, -7000.0)

# def test_cep_invalido(engenheiro_valido: Engenheiro):
#     with pytest.raises(match = "CEP inválido"):
#         Engenheiro("Crea", Genero.MASCULINO, EstadoCivil.CASADO, "DD/MM/AAAA", DadosPessoa(18, "Nome", "Telefone", "Email", 
#             Endereco("Longradouro", "Numero", "Complemento", "cep6", "Cidade", UnidadeFederativa.BAHIA)), "cpf", "rg", "Matricula", 
#             Setor.ENGENHARIA, 7000.0)
        
# def test_rg_invalido(engenheiro_valido: Engenheiro):
#     with pytest.raises(match = "RG inválido"):
#         Engenheiro("Crea", Genero.MASCULINO, EstadoCivil.CASADO, "DD/MM/AAAA", DadosPessoa(18, "Nome", "Telefone", "Email", 
#             Endereco("Longradouro", "Numero", "Complemento", "cep", "Cidade", UnidadeFederativa.BAHIA)), "cpf", "rg67", "Matricula", Setor.ENGENHARIA, 7000.0)
        

# def test_cpf_invalido(engenheiro_valido: Engenheiro):
#     with pytest.raises(match = "CPF inválido"):
#        Engenheiro("Crea", Genero.MASCULINO, EstadoCivil.CASADO, "DD/MM/AAAA", DadosPessoa(18, "Nome", "Telefone", "Email", 
#             Endereco("Longradouro", "Numero", "Complemento", "cep", "Cidade", UnidadeFederativa.BAHIA)), "cp6", "rg", "Matricula", 
#             Setor.ENGENHARIA, 7000.0)