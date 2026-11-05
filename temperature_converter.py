# Program to convert temperatures between Celsius and Fahrenheit

print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Choose an option (1 or 2): ").strip()

try:
    temperature = float(input("Enter the temperature: "))

    if choice == "1":
        converted = (temperature * 9 / 5) + 32
        print(f"Temperature in Fahrenheit: {converted:.2f} F")
    elif choice == "2":
        converted = (temperature - 32) * 5 / 9
        print(f"Temperature in Celsius: {converted:.2f} C")
    else:
        print("Invalid option. Choose 1 or 2.")

except ValueError:
    print("Please enter a valid number.")
