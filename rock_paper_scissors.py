# Rock, Paper, Scissors game
import random

choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
player = input("Choose rock, paper, or scissors: ").strip().lower()

if player not in choices:
    print("Invalid choice. Please run the game again.")
else:
    print("Computer chose:", computer)

    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("Computer wins!")
