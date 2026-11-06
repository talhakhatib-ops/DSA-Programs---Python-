# Program to manage contacts using a dictionary

contacts = {}

while True:
    print("\n1. Add or update contact")
    print("2. Search contact")
    print("3. View all contacts")
    print("4. Delete contact")
    print("5. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        name = input("Enter name: ").strip()
        phone = input("Enter phone number: ").strip()

        if name and phone:
            contacts[name] = phone
            print("Contact saved.")
        else:
            print("Name and phone number cannot be empty.")

    elif choice == "2":
        name = input("Enter name to search: ").strip()
        if name in contacts:
            print("Phone number:", contacts[name])
        else:
            print("Contact not found.")

    elif choice == "3":
        if contacts:
            for name, phone in sorted(contacts.items()):
                print(name, ":", phone)
        else:
            print("No contacts saved.")

    elif choice == "4":
        name = input("Enter name to delete: ").strip()
        if name in contacts:
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    elif choice == "5":
        print("Closing contact book.")
        break

    else:
        print("Invalid choice. Please select 1 to 5.")
