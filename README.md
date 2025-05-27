# Bank-management-system-project
A simple bank management system in Python that supports:

- Create, view, and delete Customers
- Create, view, and delete Accounts
- Perform Deposits and Withdrawals
- Search Customers by name
- List all Accounts or Customers
- All data is persisted using SQLite and managed with SQLAlchemy ORM



### Relationships:
- One-to-many: A customer can have many bank accounts
- Many-to-many: Accounts can have multiple account holders (joint accounts)

##  Technologies Used

- Python 3
- SQLAlchemy ORM
- SQLite (local database)
- CLI (Command-Line Interface)
- Pipenv (for environment and dependency management)

### set up database 
python db/setup.py

### Run CLI 
python cli.py
