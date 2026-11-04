# Program to encrypt or decrypt text using a Caesar cipher

message = input("Enter your message: ")
shift = int(input("Enter the shift value: ")) % 26
choice = input("Enter E to encrypt or D to decrypt: ").strip().lower()

if choice not in ("e", "d"):
    print("Invalid choice. Enter E or D.")
else:
    if choice == "d":
        shift = -shift

    result = ""

    for char in message:
        if "a" <= char <= "z":
            result += chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
        elif "A" <= char <= "Z":
            result += chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
        else:
            result += char

    print("Result:", result)
