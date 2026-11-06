# Program to find the number of days between two dates
from datetime import datetime

date_format = "%d-%m-%Y"

try:
    first_date_text = input("Enter the first date (DD-MM-YYYY): ")
    second_date_text = input("Enter the second date (DD-MM-YYYY): ")

    first_date = datetime.strptime(first_date_text, date_format).date()
    second_date = datetime.strptime(second_date_text, date_format).date()

    difference = abs((second_date - first_date).days)

    print("Number of days between the dates:", difference)

except ValueError:
    print("Invalid date. Please use DD-MM-YYYY, for example 06-11-2026.")
