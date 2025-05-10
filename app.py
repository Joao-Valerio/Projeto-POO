import models
import user
import product
import orders
from datetime import datetime
       
def userMenu():
    while (True):
        print("\n--- Menu Clientes ---")
        print("1 - Adicionar clientes")
        print("2 - Listar clientes")
        print("3 - Excluir clientes")
        print("4 - Atualizar clientes")
        print("0 - Voltar")
        op = input("Escolha: ")

        if op == "1":
            user.createUser()
        elif op == "2":
            user.selectUser()
        elif op == "3":
            user.deleteUser()
        elif op == "4":
            user.updateUser()
        elif op == "0":
            break
        else:
            print("Opção inválida, escolha outra")


def productsMenu():
    while (True):
        print("\n--- Menu Produtos ---")
        print("1 - Adicionar produtos")
        print("2 - Listar produtos")
        print("3 - Excluir produtos")
        print("4 - Atualizar produtos")
        print("0 - Voltar")
        op = input("Escolha: ")

        if op == "1":
            product.createProduct()
        elif op == "2":
            product.selectProduct()
        elif op == "3":
            product.deleteProduct()
        elif op == "4":
            product.updateProduct()
        elif op == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")


def ordersMenu():
    while (True):
        print("\n--- Menu de Pedidos ---")
        print("1 - Adicionar pedidos")
        print("2 - Listar pedidos")
        print("3 - Excluir pedidos")
        print("4 - Adicionar itens ao pedido")
        print("0 - Voltar")
        op = input("Escolha: ")

        if op == "1":
            orders.createOrder()
        elif op == "2":
            orders.selectOrder()
        elif op == "3":
            orders.deleteOrder()
        elif op == "4":
            orders.updateOrder()
        elif op == "0":
            break

        else:
            print("Opção inválida. Tente novamente.")        



def menu():
    while (True):
        print("\n--- Menu Principal ---")
        print("1 - Clientes")
        print("2 - Produtos")
        print("3 - Pedidos")
        print("4 - Sair")
        option = input("Escolha: ")

        if option == "1":
            userMenu()
        elif option == "2":
            productsMenu()
        elif option == "3":
            ordersMenu()
        elif option == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def clientMenu(user):
    while True:
        print("\n--- Menu Cliente ---")
        print("1 - Fazer pedido")
        print("2 - Ver meus pedidos")
        print("0 - Sair")
        op = input("Escolha: ")
        if op == "1":
            orders.createCustomerOrder(user)
        elif op == "2": 
            orders.listCustomerOrder(user)
        elif op == "0":
            break
        else:
            print("Opção inválida.")

def create():
    while (True):
        name = input("\nNome: ")
        cpf = input("Cpf: ")
        password = input("Senha: ")
        print("\n1 - Criar um cliente")
        print("2 - Criar administrador")
        op = input("Escolha: ")
        userExisting = models.User.select().where(
        (models.User.name == name) & (models.User.password == password)
    ).first()

        if userExisting:
            print("Já existe um usuário com esse nome e senha. Tente novamente.")
            return
        elif op == "1":
            models.User.create(name=name, cpf=cpf, password=password, isAdmin = False)
            print("\n Cliente criado com sucesso!")
            break
        elif op == "2":
            verificationCode = input("Crie um codigo para verificar: ")
            models.User.create(name=name, cpf=cpf, password=password, verificationCode = verificationCode, isAdmin = True)
            print("\n Admin criado com sucesso!")
            break
        else:
            print("Opcao invalida")
    

def login():
    while (True):
        print("\n1 - Entrar como Cliente")
        print("2 - Entrar como administrador")
        print("0 - Sair")
        op = input("Escolha: ")
        if op == "1":
            name = input("Usuário: ")
            password = input("Senha: ")

            currentUser = models.User.get(models.User.name == name)
            if currentUser.password == password and not currentUser.isAdmin:
                print("Login efetuado com sucesso")
                clientMenu(currentUser)
                return currentUser
            else:
                print("Senha incorreta")
        elif op == "2":
            name = input("Usuário: ")
            password = input("Senha: ")  
            code = input("Código de verificação: ")
            currentUser = models.User.get(models.User.name == name)
            if currentUser.password == password:
                if code == currentUser.verificationCode:
                    print("login como admin feito")
                    menu()
        
        elif op == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida, tente novamente")

def start():
    while (True):
        print("\n1 - Criar conta")
        print("2 - Login")
        print("0 - Sair")
        op = input("Escolha: ")
        if op == "1":
            create()
    
        elif op == "2":
            login()

        elif op == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == '__main__':
    start()