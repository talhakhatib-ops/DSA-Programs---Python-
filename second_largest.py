# Program to find the second-largest distinct number in a list

numbers = [10, 25, 8, 25, 18, 3]
unique_numbers = list(set(numbers))

if len(unique_numbers) < 2:
    print("There is no second-largest distinct number.")
else:
    unique_numbers.sort()
    print("Second-largest number:", unique_numbers[-2])
