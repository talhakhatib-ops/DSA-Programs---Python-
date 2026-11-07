# Program to implement a stack using a Python list
# Stack follows LIFO: Last In, First Out

stack = []

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        item = input("Enter an item: ")
        stack.append(item)
        print(item, "pushed onto the stack.")

    elif choice == "2":
        if stack:
            print("Popped item:", stack.pop())
        else:
            print("Stack is empty. Nothing to pop.")

    elif choice == "3":
        if stack:
            print("Top item:", stack[-1])
        else:
            print("Stack is empty.")

    elif choice == "4":
        if stack:
            print("Stack (bottom to top):", stack)
        else:
            print("Stack is empty.")

    elif choice == "5":
        print("Exiting stack program.")
        break

    else:
        print("Invalid choice. Please select 1 to 5.")
