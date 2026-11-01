# Program to convert a binary number into decimal

binary = input("Enter a binary number: ")

decimal_number = 0
valid = True

for digit in binary:
    if digit not in "01":
        valid = False
        break
    decimal_number = decimal_number * 2 + int(digit)

if not binary:
    valid = False

if valid:
    print("Decimal number:", decimal_number)
else:
    print("Invalid binary number.")
