from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Base and DB setup
Base = declarative_base()
engine = create_engine('sqlite:///bank.db')
Session = sessionmaker(bind=engine)
session = Session()

# Models
class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    accounts = relationship("Account", back_populates="customer")

    def __repr__(self):
        return f"<Customer id={self.id}, name='{self.name}'>"

class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True)
    balance = Column(Float, default=0.0)
    customer_id = Column(Integer, ForeignKey('customers.id'))

    customer = relationship("Customer", back_populates="accounts")

    def __repr__(self):
        return f"<Account id={self.id}, customer_id={self.customer_id}, balance={self.balance}>"
