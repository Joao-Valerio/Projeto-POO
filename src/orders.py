import models as models
from datetime import datetime

# Cria um pedido novo associado a um usuário
def createOrder():
    userId = input("Qual o ID do usuário que está fazendo o pedido: ")
    user = models.User.get_by_id(userId)
    newOrder = models.Order.create(
    user=user, orderDate=datetime.now(), totalPrice=0.0)
    print(f"Pedido {newOrder.id} criado para o cliente {user.name}.")
    itemsOrder(newOrder)

# Lista todos os pedidos com dados do cliente
def selectOrder():
    print("\n--- Lista de Pedidos ---")
    for order in models.Order.select(models.User, models.Order).join(models.User).order_by(models.Order.id):
        print(f"ID: {order.id}, Cliente: {order.user.name} (ID: {order.user.id}), "
        f"Data: {order.orderDate.strftime('%d/%m/%Y %H:%M:%S')}, Total: R$ {order.totalPrice:.2f}")

# Exclui um pedido
def deleteOrder():
    orderId = input("Qual ID do pedido a ser excluido: ")
    order = models.Order.get_by_id(orderId)
    order.delete_instance()
    print("Pedido excluído com sucesso!")

# Adiciona mais itens a um pedido
def updateOrder():
    orderId = input("ID do pedido para adicionar itens: ")
    if models.Order.select().where(models.Order.id == orderId).exists():
        pedido = models.Order.get_by_id(orderId)
        itemsOrder(pedido)
    else:
        print("Pedido não encontrado.")

# Adiciona itens a um pedido
def itemsOrder(pedido):
    while True:
        productName = input("Nome do produto a adicionar (0 para terminar): ")
        if productName == "0":
            break
        elif models.Product.select().where(models.Product.productName == productName).exists():
            product = models.Product.get(models.Product.productName == productName)
            quantidade = int(input("Quantidade: "))
            models.ProductOrder.create(pedido=pedido, produto=product, quantidade=quantidade)
            print(f"{quantidade}x {product.productName} adicionado(s) ao pedido {pedido.id}.")
            pedido.totalPrice += float(product.price) * quantidade
            pedido.save()
        else:
            print("Produto não encontrado.")

# Lista pedidos de um cliente específico
def listCustomerOrder(user):
    print(f"\n--- Lista de Pedidos do cliente {user} ---")
    orders = models.Order.select().where(models.Order.user == user).order_by(models.Order.id)

    if not orders:
        print("Nenhum pedido encontrado.")
        return

    for order in orders:
        print(f"ID: {order.id}, Cliente: {order.user.name} (ID: {order.user.id}), "
              f"Data: {order.orderDate.strftime('%d/%m/%Y %H:%M:%S')}, Total: R$ {order.totalPrice:.2f}")
    
# Cria pedido direto para cliente logado   
def createCustomerOrder(user):
    newOrder = models.Order.create(
    user=user, orderDate=datetime.now(), totalPrice=0.0)
    print(f"Pedido {newOrder.id} criado para o cliente {user.name}.")
    itemsOrder(newOrder)   
    