

import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models import session
from models.customer import Customer
from models.account import Account


c1 = Customer(name="Lydia", email="lydia@example.com")
a1 = Account(balance=1000.0, customer=c1)

c2 = Customer(name="Ayitsoh", email="ayitsoh@school.com")
a2 = Account(balance=500.0, customer=c2)


session.add_all([c1, a1, c2, a2])
session.commit()

print("Data inserted successfully!")
