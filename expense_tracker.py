# Simple expense tracker using a list and dictionaries

expenses = []

while True:
    print("\n1. Add expense")
    print("2. View expenses")
    print("3. Show total")
    print("4. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        category = input("Enter expense category: ").strip()

        try:
            amount = float(input("Enter amount: "))
            if not category or amount <= 0:
                print("Enter a category and an amount greater than zero.")
            else:
                expenses.append({"category": category, "amount": amount})
                print("Expense added.")
        except ValueError:
            print("Please enter a valid amount.")

    elif choice == "2":
        if not expenses:
            print("No expenses recorded.")
        else:
            for index, expense in enumerate(expenses, start=1):
                print(f"{index}. {expense['category']}: {expense['amount']:.2f}")

    elif choice == "3":
        total = sum(expense["amount"] for expense in expenses)
        print(f"Total expenses: {total:.2f}")

    elif choice == "4":
        print("Thank you for using the expense tracker.")
        break

    else:
        print("Invalid option. Choose from 1 to 4.")
