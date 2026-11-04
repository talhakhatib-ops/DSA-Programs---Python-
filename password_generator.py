# Program to generate a random password

import secrets
import string

length = int(input("Enter password length (minimum 8): "))

if length < 8:
    print("Please choose a length of at least 8 characters.")
else:
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(characters) for _ in range(length))

    print("Generated password:", password)
