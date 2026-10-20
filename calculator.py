# Simple calculator for two numbers

num1 = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

if operator == "+":
    print("Result:", num1 + num2)
elif operator == "-":
    print("Result:", num1 - num2)
elif operator == "*":
    print("Result:", num1 * num2)
elif operator == "/":
    if num2 == 0:
        print("Error: Cannot divide by zero.")
    else:
        print("Result:", num1 / num2)
else:
    print("Invalid operator.")
