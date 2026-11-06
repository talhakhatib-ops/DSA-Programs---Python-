# Program to implement a queue using collections.deque
from collections import deque

queue = deque()

while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Display queue")
    print("4. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        item = input("Enter an item: ")
        queue.append(item)
        print(item, "added to the queue.")

    elif choice == "2":
        if queue:
            print("Removed item:", queue.popleft())
        else:
            print("Queue is empty.")

    elif choice == "3":
        if queue:
            print("Queue (front to rear):", list(queue))
        else:
            print("Queue is empty.")

    elif choice == "4":
        print("Exiting queue program.")
        break

    else:
        print("Invalid choice. Please select 1 to 4.")
