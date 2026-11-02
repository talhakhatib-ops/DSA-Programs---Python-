# Program to convert a decimal number into binary

number = int(input("Enter a non-negative decimal number: "))

if number < 0:
    print("Please enter a non-negative number.")
elif number == 0:
    print("Binary number: 0")
else:
    binary = ""
    while number > 0:
        remainder = number % 2
        binary = str(remainder) + binary
        number //= 2

    print("Binary number:", binary)
