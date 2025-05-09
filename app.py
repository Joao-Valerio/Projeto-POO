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


if __name__ == '__main__':
    menu()