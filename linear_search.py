# Program to search for an element in a predefined list using linear search

numbers = [10, 20, 30, 40, 50]
target = int(input("Enter the number to search for: "))

found = False

for index in range(len(numbers)):
    if numbers[index] == target:
        print("Element found at index:", index)
        found = True
        break

if not found:
    print("Element not found.")
