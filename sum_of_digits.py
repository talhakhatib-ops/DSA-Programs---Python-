# Program to calculate the sum of the digits of a number

number = abs(int(input("Enter an integer: ")))
total = 0

while number > 0:
    digit = number % 10
    total += digit
    number //= 10

print("Sum of digits:", total)
