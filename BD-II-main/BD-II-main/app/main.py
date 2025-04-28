import os
from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.connection import Session

os.system("cls || clear")

def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    # Criando um usuario
    service.criar_usuario("Marta", "marta@gmail.com", "123")

    # Listando todos os usuarios
    print("\nListando todos os usuarios")
    lista_usuarios = service.listar_todos_usuarios()
    for  usuario in lista_usuarios:
        print(f"\n{usuario.id} \nNome: {usuario.nome} \nE-mail: {usuario.email} \nSenha: {usuario.senha}")

if __name__ == "__main__":
    main()