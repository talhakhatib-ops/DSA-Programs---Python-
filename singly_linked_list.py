# Program to create and manage a singly linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    def display(self):
        if self.head is None:
            print("The linked list is empty.")
            return

        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def search(self, target):
        current = self.head
        position = 1

        while current is not None:
            if current.data == target:
                return position
            current = current.next
            position += 1

        return -1

    def delete(self, target):
        if self.head is None:
            return False

        if self.head.data == target:
            self.head = self.head.next
            return True

        current = self.head
        while current.next is not None:
            if current.next.data == target:
                current.next = current.next.next
                return True
            current = current.next

        return False


linked_list = LinkedList()

while True:
    print("\n1. Insert at end")
    print("2. Display")
    print("3. Search")
    print("4. Delete first matching value")
    print("5. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        value = input("Enter a value: ")
        linked_list.append(value)
        print("Value inserted.")

    elif choice == "2":
        linked_list.display()

    elif choice == "3":
        value = input("Enter a value to search: ")
        position = linked_list.search(value)

        if position == -1:
            print("Value not found.")
        else:
            print("Value found at position:", position)

    elif choice == "4":
        value = input("Enter a value to delete: ")
        if linked_list.delete(value):
            print("Value deleted.")
        else:
            print("Value not found.")

    elif choice == "5":
        print("Exiting linked list program.")
        break

    else:
        print("Invalid choice. Please select 1 to 5.")
