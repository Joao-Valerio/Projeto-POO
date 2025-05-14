import models as models
import app as app

# Função para login de administradores
def loginAdmin():
    name = input("Usuário: ")
    password = input("Senha: ")  
    code = input("Código de verificação: ")
    currentUser = models.User.get(models.User.name == name)
    if currentUser.password == password:
        if code == currentUser.verificationCode:
            print("login como admin feito")

# Função para login de clientes (usuários comuns)
def loginClient():
            name = input("Usuário: ")
            password = input("Senha: ")

            currentUser = models.User.get(models.User.name == name)
            if currentUser.password == password and not currentUser.isAdmin:
                print("Login efetuado com sucesso")
                app.clientMenu(currentUser)
                return currentUser
            else:
                print("Senha incorreta")