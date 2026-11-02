# Program to find the GCD of two numbers using the Euclidean algorithm

num1 = abs(int(input("Enter the first number: ")))
num2 = abs(int(input("Enter the second number: ")))

while num2 != 0:
    num1, num2 = num2, num1 % num2

print("GCD:", num1)
