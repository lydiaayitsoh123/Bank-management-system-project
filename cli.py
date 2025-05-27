from models import session
from models.customer import Customer
from models.account import Account
from models.transaction import Transaction

def menu():
    while True:
        print("\nBank CLI")
        print("1. Create Customer")
        print("2. Create Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. View Customers")
        print("6. Exit")
        choice = input("> ")

        if choice == '1':
            name = input("Name: ")
            email = input("Email: ")
            customer = Customer(name=name, email=email)
            session.add(customer)
            session.commit()
            print("Customer created.")

        elif choice == '2':
            customer_id = int(input("Customer ID: "))
            acc = Account(customer_id=customer_id, balance=0.0)
            session.add(acc)
            session.commit()
            print("Account created.")

        elif choice == '3':
            acc_id = int(input("Account ID: "))
            amount = float(input("Amount: "))
            acc = session.get(Account, acc_id)
            acc.balance += amount
            session.add(Transaction(type="deposit", amount=amount, account=acc))
            session.commit()
            print("Deposit successful.")

        elif choice == '4':
            acc_id = int(input("Account ID: "))
            amount = float(input("Amount: "))
            acc = session.get(Account, acc_id)
            if acc.balance >= amount:
                acc.balance -= amount
                session.add(Transaction(type="withdrawal", amount=amount, account=acc))
                session.commit()
                print("Withdrawal successful.")
            else:
                print("Insufficient balance.")

        elif choice == '5':
            customers = session.query(Customer).all()
            for c in customers:
                print(c)

        elif choice == '6':
            break

if __name__ == "__main__":
    menu()
