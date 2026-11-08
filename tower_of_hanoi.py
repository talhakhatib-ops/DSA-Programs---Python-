# Program to solve the Tower of Hanoi using recursion

def tower_of_hanoi(disks, source, auxiliary, destination):
    if disks == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return 1

    moves = tower_of_hanoi(disks - 1, source, destination, auxiliary)
    print(f"Move disk {disks} from {source} to {destination}")
    moves += 1
    moves += tower_of_hanoi(disks - 1, auxiliary, source, destination)

    return moves


try:
    number_of_disks = int(input("Enter the number of disks (1-10): "))

    if 1 <= number_of_disks <= 10:
        total_moves = tower_of_hanoi(
            number_of_disks, "A", "B", "C"
        )
        print("Total moves:", total_moves)
    else:
        print("Please enter a number between 1 and 10.")

except ValueError:
    print("Please enter a whole number.")
