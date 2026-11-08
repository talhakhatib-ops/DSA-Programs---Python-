# Simple bank account simulator using a Python class

class BankAccount:
    def __init__(self, opening_balance=0):
        self.balance = opening_balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
        else:
            self.balance += amount
            print(f"Deposited: Rs. {amount:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrawn: Rs. {amount:.2f}")

    def show_balance(self):
        print(f"Current balance: Rs. {self.balance:.2f}")


account = BankAccount()

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check balance")
    print("4. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        try:
            amount = float(input("Enter deposit amount: Rs. "))
            account.deposit(amount)
        except ValueError:
            print("Please enter a valid amount.")

    elif choice == "2":
        try:
            amount = float(input("Enter withdrawal amount: Rs. "))
            account.withdraw(amount)
        except ValueError:
            print("Please enter a valid amount.")

    elif choice == "3":
        account.show_balance()

    elif choice == "4":
        print("Thank you for using the bank account simulator.")
        break

    else:
        print("Invalid choice. Please select 1 to 4.")
