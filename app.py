import models
from datetime import datetime

def createUser():
    name = input("Nome: ")
    cpf = input("Cpf: ")
    models.User.create(name=name, cpf=cpf)

def selectUser():
    print("\n--- Lista de Clientes ---")
    for user in models.User.select():
        print(f"{user.id} - {user.name} ({user.cpf})")

def deleteUser():
    userID = input("Informe o ID do cliente a ser excluido: ")
    user = models.User.get_by_id(userID)  
    user.delete_instance()
    print("Cliente excluído com sucesso!")

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

def createProduct():
    productName = input("Qual o nome do produto: ")
    price = input("Informe o preço do produto: ")
    models.Product.create(productName=productName, price=price)

def selectProduct():
    print("\n--- Lista de Produtos ---")
    for products in models.Product.select():
        print(f"{products.id} - {products.productName} - {products.price}")

def deleteProduct():
    productId = input("Informe o ID do produto a ser excluido: ")
    product = models.Product.get_by_id(productId)
    product.delete_instance()
    print("Produto excluído com sucesso!")

def updateProduct():
    productId = input("ID do produto a ser atualizado: ")
    if models.Product.select().where(models.Product.id == productId).exists():
        product = models.Product.get_by_id(productId)
        newName = input("Novo nome do produto: ")
        newPrice = input("Novo preço: ")
        product.productName = newName
        product.price = newPrice
        product.save()
        print("Produto atualizado com sucesso!")
    else:
        print("Produto não encontrado.")

def createOrder():
    userId = input("Qual o ID do usuário que está fazendo o pedido: ")
    user = models.User.get_by_id(userId)
    newOrder = models.Order.create(
    user=user, orderDate=datetime.now(), totalPrice=0.0)
    print(f"Pedido {newOrder.id} criado para o cliente {user.name}.")
    itemsOrder(newOrder)

def selectOrder():
    print("\n--- Lista de Pedidos ---")
    for order in models.Order.select(models.User, models.Order).join(models.User).order_by(models.Order.id):
        print(f"ID: {order.id}, Cliente: {order.user.name} (ID: {order.user.id}), "
        f"Data: {order.orderDate.strftime('%d/%m/%Y %H:%M:%S')}, Total: R$ {order.totalPrice:.2f}")

def deleteOrder():
    orderId = input("Qual ID do pedido a ser excluido: ")
    order = models.Order.get_by_id(orderId)
    order.delete_instance()
    print("Pedido excluído com sucesso!")

def updateOrder():
    orderId = input("ID do pedido para adicionar itens: ")
    if models.Order.select().where(models.Order.id == orderId).exists():
        pedido = models.Order.get_by_id(orderId)
        itemsOrder(pedido)
    else:
        print("Pedido não encontrado.")
        
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
            createUser()
        elif op == "2":
            selectUser()
        elif op == "3":
            deleteUser()
        elif op == "4":
            updateUser()
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
            createProduct()
        elif op == "2":
            selectProduct()
        elif op == "3":
            deleteProduct()
        elif op == "4":
            updateProduct()
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
            createOrder()
        elif op == "2":
            selectOrder()
        elif op == "3":
            deleteOrder()
        elif op == "4":
            updateOrder()
        elif op == "0":
            break

        else:
            print("Opção inválida. Tente novamente.")        

def itemsOrder(pedido):
    while True:
        productId = input("ID do produto a adicionar (0 para terminar): ")
        if productId == "0":
            break
        if models.Product.select().where(models.Product.id == productId).exists():
            product = models.Product.get_by_id(productId)
            quantidade = int(input("Quantidade: "))
            models.ProductOrder.create(pedido=pedido, produto=product, quantidade=quantidade)
            print(f"{quantidade}x {product.productName} adicionado(s) ao pedido {pedido.id}.")
            pedido.totalPrice += float(product.price) * quantidade
            pedido.save()
        else:
            print("Produto não encontrado.")

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