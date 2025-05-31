from sqlalchemy.orm import relationship
from models import Base
from sqlalchemy import Column, Integer, String

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

    accounts = relationship("Account", back_populates="customer")
def __repr__(self):
    return f"<Customer(id={self.id}, name='{self.name}', email='{self.email}')>"


def __str__(self):
    return f"{self.name} (ID: {self.id})"
