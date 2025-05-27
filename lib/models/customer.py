from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)

    accounts = relationship("Account", back_populates="customer")

    def __repr__(self):
        return f"<Customer(name={self.name}, email={self.email})>"
