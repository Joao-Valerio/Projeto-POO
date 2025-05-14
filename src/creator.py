import models as models

# Menu de criação de conta
def creator():
    name = input("\nNome: ")
    cpf = input("Cpf: ")
    password = input("Senha: ")

    userExisting = models.User.select().where(
        (models.User.name == name) & (models.User.password == password)
    ).first()

    if userExisting:
        print("Já existe um usuário com esse nome e senha. Tente novamente.")
        return

    print("\n1 - Criar Cliente")
    print("2 - Criar Administrador")
    option = input("Escolha: ")

    if option == "1":
        creatorClient(name, cpf, password)
    elif option == "2":
        creatorAdmin(name, cpf, password)
    else:
        print("Opção inválida")


# Cria cliente comum
def creatorClient(name, cpf, password):
    models.User.create(name=name, cpf=cpf, password=password, isAdmin=False)
    print("\nCliente criado com sucesso!")

# Cria administrador com código de verificação
def creatorAdmin(name, cpf, password):
    verificationCode = input("Crie um código de verificação: ")
    models.User.create(name=name, cpf=cpf, password=password, verificationCode=verificationCode, isAdmin=True)
    print("\nAdministrador criado com sucesso!")
