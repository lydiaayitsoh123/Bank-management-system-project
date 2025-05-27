from models import session
from models.customer import Customer
from models.account import Account

c1 = Customer(name="Alice", email="alice@example.com")
a1 = Account(balance=1000.0, customer=c1)

session.add_all([c1, a1])
session.commit()
