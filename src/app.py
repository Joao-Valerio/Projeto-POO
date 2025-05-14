import user as user
import product as product
import orders as orders
import logins as logins
import creator as creator
       
def userMenu():
    while (True):
        print("\n--- Menu Clientes ---")
        print("1 - Adicionar clientes")
        print("2 - Listar clientes")
        print("3 - Excluir clientes")
        print("4 - Atualizar clientes")
        print("0 - Voltar")
        option = input("Escolha: ")

        if option == "1":
            user.createUser()
        elif option == "2":
            user.selectUser()
        elif option == "3":
            user.deleteUser()
        elif option == "4":
            user.updateUser()
        elif option == "0":
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
        option = input("Escolha: ")

        if option == "1":
            product.createProduct()
        elif option == "2":
            product.selectProduct()
        elif option == "3":
            product.deleteProduct()
        elif option == "4":
            product.updateProduct()
        elif option == "0":
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
        option = input("Escolha: ")

        if option == "1":
            orders.createOrder()
        elif option == "2":
            orders.selectOrder()
        elif option == "3":
            orders.deleteOrder()
        elif option == "4":
            orders.updateOrder()
        elif option == "0":
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
        option = input("Escolha: ")
        if option == "1":
            orders.createCustomerOrder(user)
        elif option == "2": 
            orders.listCustomerOrder(user)
        elif option == "0":
            break
        else:
            print("Opção inválida.")

def create():
    while (True):
        creator.creator()

def login():
    while (True):
        print("\n1 - Entrar como Cliente")
        print("2 - Entrar como administrador")
        print("0 - Sair")
        option = input("Escolha: ")
        if option == "1":
            logins.loginClient()
        elif option == "2":
            logins.loginAdmin()
            menu()
        
        elif option == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida, tente novamente")

def start():
    while (True):
        print("\n1 - Criar conta")
        print("2 - Login")
        print("0 - Sair")
        option = input("Escolha: ")
        if option == "1":
            create()
    
        elif option == "2":
            login()

        elif option == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == '__main__':
    start() 