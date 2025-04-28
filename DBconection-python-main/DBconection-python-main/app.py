import os
import time

# Cores de texto
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
ORANGE = "\033[38;5;214m"
CIANO = "\033[96m"
PINK = "\033[35m"
RESET = "\033[0m"

def limpa_tela():
    os.system("cls || clear")
    print(f" {CIANO}*==== BEM VINDO A BANQUETOLA ====*{RESET}\n")


def color_menu():
    limpa_tela()
    print(f"{CIANO} |================================|{RESET}")
    print(f"{CIANO} |       MENU DE OPÇÕES           |{RESET}")
    print(f"{CIANO} |================================|{RESET}")
    print(f"{GREEN} | 1 | CREATE - Salvar            |{RESET}")
    print(f"{BLUE} | 2 | UPDATE  - Atualizar        |{RESET}")
    print(f"{RED} | 3 | DELETE - Deletar           |{RESET}")
    print(f"{ORANGE} | 4 | ONLY READ - Consulta única |{RESET}")
    print(f"{YELLOW} | 5 | ALL READ - Consulta geral  |{RESET}")
    print(f"{CIANO} |================================|{RESET}")
    print(f"{PINK} | 6 |     PARAR O PROGRAMA       |{RESET}")
    print(f"{CIANO} |================================|{RESET}")

# Create - Insert - Salvar == 1
def create():
    time.sleep(5)
    limpa_tela()
    print("\n*== CADASTRO DE NOVO USUARIO ==* ")
    inserir_nome = input("Digite seu nome: ")
    inserir_sobrenome = input("Digite seu sobrenome: ")
    inserir_email = input("Digite seu email: ")
    inserir_senha = input("Digite sua senha: ")

    cliente = Cliente(nome=inserir_nome, sobrenome=inserir_sobrenome, email=inserir_email, senha=inserir_senha)
    session.add(cliente)
    session.commit()


# U - Update - UPDATE - Atualizar == 2
def update():
    time.sleep(5)
    limpa_tela()
    print("\n*== ATUALIZAR DADOS DO USUARIO ==* ")
    email_cliente = input("\nDigite o e-mail do cliente que será atualizado: ")

    cliente = session.query(Cliente).filter_by(email = email_cliente).first()

    if cliente:
        cliente.nome = input("Digite seu nome: ")
        cliente.sobrenome = input("Digite seu sobrenome: ")
        cliente.email = input("Digite seu email: ")
        cliente.senha = input("Digite sua senha: ")

        session.commit()

    else:
        print("Cliente não encontrado. ")

# D - Delete - DELETE - Excluir == 3
def delete():
    time.sleep(5)
    limpa_tela()
    print("\n*== EXCLUIR DADOS DO USUARIO ==*")
    email_cliente = input("\nDigite o e-mail do cliente que será excluído: ")

    cliente = session.query(Cliente).filter_by(email = email_cliente).first()

    if cliente:
        session.delete(cliente)
        session.commit()
        print(f"Cliente {cliente.nome} excluido com sucesso!")

    else:
        print("Cliente não encontrado. ")

# R - Read - Select - Consulta (UNICA) == 4
def only_read():
        limpa_tela()
        print("\n*== CONSULTAR DADOS DO USUARIO ==*")
        email_cliente = input("\nDigite o e-mail do cliente: ")

        cliente = session.query(Cliente).filter_by(email = email_cliente).first()

        if cliente:
            print(f"R.A.:{cliente.ra} \nNome completo: {cliente.nome} {cliente.sobrenome} \nE-mail: {cliente.email} \nSenha: {cliente.senha}")
        else:
            print("Cliente não encontrado!")

        input("\nAperte qualquer tecla para voltar ao menu de opções! ")

# R - Read - Select - Consulta geral == 5
def all_read():
    limpa_tela()
    print("\n*== EXIBINDO DADOS DE TODOS OS USUARIOS ==*")
    lista_clientes = session.query(Cliente).all()

    for cliente in lista_clientes:
        print(f"\n\nR.A.:{cliente.ra} \nNome completo: {cliente.nome} {cliente.sobrenome} \nE-mail: {cliente.email} \nSenha: {cliente.senha}")

    input("\nAperte qualquer tecla para voltar ao menu de opções!")

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dados
BANQUETINHA = create_engine("sqlite:///banquetinha.db")

# Criando conexão com banco de dados
Session = sessionmaker(bind=BANQUETINHA)
session = Session()

# Criando tabela
Base = declarative_base()

class Cliente(Base):
    __tablename__ = "clientes"

    # Definindo campos da tabela.
    ra =  Column("ra", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    sobrenome = Column("sobrenome", String)
    email = Column("email", String)
    senha = Column("senha", String)

    # Definindo atributos da classe
    def __init__(self, nome: str, sobrenome: str, email: str, senha: str):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.senha = senha

# Criando tabela no banco de dados
Base.metadata.create_all(bind=BANQUETINHA)

# CRUD
editar = True

while editar:
    color_menu()
    opcao = int(input(f"{GREEN}\n\n - Informe a opção desejada de acordo com o menu: {RESET}"))

    match (opcao):
        case 1:
            criar = create()        
        case 2:
            atualizar = update()
        case 3:
            deletar = delete()
        case 4:
            consulta_unica = only_read()
        case 5:
            consulta_geral = all_read()
        case 6:
            print("Programa encerrado!")
            break
        case _:
            print("Opção invalida!")

# Fechando conexão
session.close()