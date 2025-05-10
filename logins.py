import models
import app

def loginAdmin():
    name = input("Usuário: ")
    password = input("Senha: ")  
    code = input("Código de verificação: ")
    currentUser = models.User.get(models.User.name == name)
    if currentUser.password == password:
        if code == currentUser.verificationCode:
            print("login como admin feito")

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