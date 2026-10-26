# Program to check whether a number is an Armstrong number

number = int(input("Enter a non-negative integer: "))
original = number
digits = len(str(number))
total = 0

if number < 0:
    print("Please enter a non-negative integer.")
else:
    while number > 0:
        digit = number % 10
        total += digit ** digits
        number //= 10

    if total == original:
        print("Armstrong number")
    else:
        print("Not an Armstrong number")
