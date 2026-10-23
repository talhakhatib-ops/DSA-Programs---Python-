# Program to count the frequency of each character in a string

text = input("Enter a word or sentence: ")
frequency = {}

for char in text:
    if char != " ":
        frequency[char] = frequency.get(char, 0) + 1

for char, count in frequency.items():
    print(char, ":", count)
