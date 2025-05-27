import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))



from models import Customer, Account
from helper import (
    create_record,
    get_all,
    get_by_id,
    delete_by_id,
    find_by_name,
    update_record
)

def create_customer():
    name = input("Enter customer name: ")
    if not name.strip():
        print(" Name cannot be empty.")
        return
    customer = Customer(name=name)
    create_record(customer)
    print(f"✅ Customer '{name}' added with ID {customer.id}.")

def create_account():
    customer_id = input("Enter customer ID to create an account for: ")
    customer = get_by_id(Customer, customer_id)
    if customer:
        account = Account(customer=customer)
        create_record(account)
        print(f"✅ Account created with ID {account.id} for customer '{customer.name}'.")
    else:
        print(" Customer not found.")

def deposit():
    account_id = input("Enter account ID: ")
    account = get_by_id(Account, account_id)
    if not account:
        print(" Account not found.")
        return
    amount = float(input("Enter amount to deposit: "))
    if amount <= 0:
        print("Amount must be positive.")
        return
    account.balance += amount
    update_record()
    print(f"✅ Deposited {amount}. New balance: {account.balance}")

def withdraw():
    account_id = input("Enter account ID: ")
    account = get_by_id(Account, account_id)
    if not account:
        print(" Account not found.")
        return
    amount = float(input("Enter amount to withdraw: "))
    if amount <= 0:
        print(" Amount must be positive.")
        return
    if account.balance >= amount:
        account.balance -= amount
        update_record()
        print(f"✅ Withdrew {amount}. New balance: {account.balance}")
    else:
        print(" Insufficient funds.")

def list_customers():
    customers = get_all(Customer)
    if customers:
        for c in customers:
            print(c)
    else:
        print(" No customers found.")

def list_accounts():
    accounts = get_all(Account)
    if accounts:
        for a in accounts:
            print(a)
    else:
        print(" No accounts found.")

def delete_customer():
    customer_id = input("Enter customer ID to delete: ")
    if delete_by_id(Customer, customer_id):
        print("✅ Customer deleted.")
    else:
        print(" Customer not found.")

def delete_account():
    account_id = input("Enter account ID to delete: ")
    if delete_by_id(Account, account_id):
        print("✅Account deleted.")
    else:
        print(" Account not found.")

def find_customer():
    name = input("Enter customer name to search: ")
    results = find_by_name(Customer, name)
    if results:
        for c in results:
            print(c)
    else:
        print(" No matching customers found.")

def menu():
    while True:
        print("\n BANK MANAGEMENT SYSTEM MENU")
        print("1. Create Customer")
        print("2. Create Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. List All Customers")
        print("6. List All Accounts")
        print("7. Delete Customer")
        print("8. Delete Account")
        print("9. Find Customer by Name")
        print("0. Exit")
        choice = input("👉 Choose an option: ")

        if choice == "1":
            create_customer()
        elif choice == "2":
            create_account()
        elif choice == "3":
            deposit()
        elif choice == "4":
            withdraw()
        elif choice == "5":
            list_customers()
        elif choice == "6":
            list_accounts()
        elif choice == "7":
            delete_customer()
        elif choice == "8":
            delete_account()
        elif choice == "9":
            find_customer()
        elif choice == "0":
            print(" Exiting. Goodbye!")
            break
        else:
            print(" Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
