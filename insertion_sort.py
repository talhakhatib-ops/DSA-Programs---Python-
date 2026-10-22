# Program to sort a predefined list using Insertion Sort

numbers = [5, 2, 8, 1, 3]

for i in range(1, len(numbers)):
    current = numbers[i]
    j = i - 1

    while j >= 0 and numbers[j] > current:
        numbers[j + 1] = numbers[j]
        j -= 1

    numbers[j + 1] = current

print("Sorted list:", numbers)
