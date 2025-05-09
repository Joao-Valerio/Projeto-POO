import models
from datetime import datetime

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