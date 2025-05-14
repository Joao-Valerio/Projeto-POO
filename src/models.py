from peewee import *
from datetime import datetime

myDb = SqliteDatabase("dados.db")


class BaseModel(Model):
    class Meta:
        database = myDb


class User(BaseModel):
    name = CharField()
    cpf = CharField(unique=True)
    password = CharField()
    verificationCode = CharField(unique = True, null = True)
    isAdmin = BooleanField(default=False)

    def __str__(self):
        return f"{self.id} - {self.name} ({self.cpf})"

class Order(BaseModel):
    user = ForeignKeyField(User, backref='pedidos')
    orderDate = DateTimeField(default=datetime.now)
    totalPrice = FloatField()

    def __str__(self):
        return f"Pedido {self.id} | Cliente: {self.user.name} | Data: {self.orderDate.strftime('%d/%m/%Y %H:%M:%S')} | Total: R$ {self.totalPrice:.2f}"


class Product(BaseModel):
    price = FloatField()
    productName = CharField()

    def __str__(self):
        return f"{self.id} - {self.productName} (R$ {self.price:.2f})"

class ProductOrder(BaseModel):
    pedido = ForeignKeyField(Order, backref='itens')
    produto = ForeignKeyField(Product)
    quantidade = IntegerField(default=1)

    def __str__(self):
        return f"{self.quantidade}x {self.produto.productName} (R$ {self.produto.price:.2f} cada)"

myDb.connect()
myDb.create_tables([User, Product, Order, ProductOrder])