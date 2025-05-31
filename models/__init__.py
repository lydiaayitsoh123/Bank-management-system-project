

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("sqlite:///bank.db", echo=False)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


from .customer import Customer
from .account import Account
