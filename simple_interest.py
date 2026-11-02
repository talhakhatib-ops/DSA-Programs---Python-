# Program to calculate simple interest

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual rate of interest: "))
time = float(input("Enter the time in years: "))

interest = (principal * rate * time) / 100

print("Simple interest:", interest)
print("Total amount:", principal + interest)
