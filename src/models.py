from peewee import *
from datetime import datetime

# Cria ou conecta ao banco de dados SQLite
myDb = SqliteDatabase("dados.db")

# Classe base para os modelos
class BaseModel(Model):
    class Meta:
        database = myDb

# Tabela de usuários (clientes e administradores)
class User(BaseModel):
    name = CharField()
    cpf = CharField(unique=True)
    password = CharField()
    verificationCode = CharField(unique = True, null = True)
    isAdmin = BooleanField(default=False)

    def __str__(self):
        return f"{self.id} - {self.name} ({self.cpf})"

# Tabela de pedidos
class Order(BaseModel):
    user = ForeignKeyField(User, backref='pedidos')
    orderDate = DateTimeField(default=datetime.now)
    totalPrice = FloatField()

    def __str__(self):
        return f"Pedido {self.id} | Cliente: {self.user.name} | Data: {self.orderDate.strftime('%d/%m/%Y %H:%M:%S')} | Total: R$ {self.totalPrice:.2f}"

# Tabela de produtos
class Product(BaseModel):
    price = FloatField()
    productName = CharField()

    def __str__(self):
        return f"{self.id} - {self.productName} (R$ {self.price:.2f})"

# Tabela de itens do pedido (produto + quantidade)
class ProductOrder(BaseModel):
    pedido = ForeignKeyField(Order, backref='itens')
    produto = ForeignKeyField(Product)
    quantidade = IntegerField(default=1)

    def __str__(self):
        return f"{self.quantidade}x {self.produto.productName} (R$ {self.produto.price:.2f} cada)"

# Conecta ao banco e cria as tabelas, se não existirem
myDb.connect()
myDb.create_tables([User, Product, Order, ProductOrder])