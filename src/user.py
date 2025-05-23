import models as models

# Cria um novo cliente (usuário comum)
def createUser():
    name = input("Nome: ")
    cpf = input("Cpf: ")
    password = input("Senha: ")
    models.User.create(name=name, cpf=cpf, password=password)
    print("\n Cliente criado com sucesso!")

# Lista todos os usuários cadastrados
def selectUser():
    print("\n--- Lista de Clientes ---")
    for user in models.User.select():
        print(f"{user.id} - {user.name} ({user.cpf})")

# Exclui um usuário pelo ID
def deleteUser():
    userID = input("Informe o ID do cliente a ser excluido: ")
    user = models.User.get_by_id(userID)  
    user.delete_instance()
    print("Cliente excluído com sucesso!")

# Atualiza nome e CPF de um cliente
def updateUser():
    userID = input("Informe o ID do cliente a ser atualizado: ")
    if models.User.select().where(models.User.id == userID).exists():
        user = models.User.get_by_id(userID)
        newName = input("Novo nome: ")
        newCpf = input("Novo CPF: ")
        user.name = newName
        user.cpf = newCpf
        user.save()
        print("Cliente atualizado com sucesso!")
    else:
        print("Cliente não encontrado.")