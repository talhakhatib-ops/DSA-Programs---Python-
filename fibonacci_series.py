# Program to print the first n terms of the Fibonacci series

n = int(input("How many terms do you want? "))

first = 0
second = 1

if n <= 0:
    print("Please enter a positive number of terms.")
else:
    for i in range(n):
        print(first, end=" ")
        first, second = second, first + second
    print()
