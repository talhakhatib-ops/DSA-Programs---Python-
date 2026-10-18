# Program to search for an element in a list using linear search

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
target = int(input("Enter the number to search for: "))

found = False

for index in range(len(numbers)):
    if numbers[index] == target:
        print("Number found at index:", index)
        found = True
        break

if not found:
    print("Number not found.")
