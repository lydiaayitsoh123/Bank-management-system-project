from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base
from .account import Account

class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    amount = Column(Float)
    type = Column(String)  # 'deposit' or 'withdrawal'
    account_id = Column(Integer, ForeignKey('accounts.id'))

    account = relationship("Account", back_populates="transactions")

    def __repr__(self):
        return f"<Transaction(type={self.type}, amount={self.amount})>"
