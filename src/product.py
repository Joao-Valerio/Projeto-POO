import models as models

def createProduct():
    productName = input("Qual o nome do produto: ")
    price = input("Informe o preço do produto: ")
    models.Product.create(productName=productName, price=price)
    print("\n Produto criado com sucesso!")

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