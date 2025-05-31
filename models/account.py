from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from models import Base

class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True)
    balance = Column(Float, default=0.0)
    customer_id = Column(Integer, ForeignKey('customers.id'))

    customer = relationship("Customer", back_populates="accounts")
