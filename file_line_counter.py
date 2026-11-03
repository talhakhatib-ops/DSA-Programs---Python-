# Program to count lines in a text file

filename = input("Enter the text file name: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        line_count = sum(1 for line in file)
    print("Number of lines:", line_count)
except FileNotFoundError:
    print("File not found. Check the file name and try again.")
