import random

choices = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0

while True:
    print("\nScore -> You:", player_score, "| Computer:", computer_score)

    player = input("Choose rock, paper, scissors (or 'quit'): ").lower()

    if player == "quit":
        print("\nFinal Score:")
        print("You:", player_score)
        print("Computer:", computer_score)
        break

    if player not in choices:
        print("Invalid choice! Try again.")
        continue

    computer = random.choice(choices)

    print("You chose:", player)
    print("Computer chose:", computer)

    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win this round!")
        player_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1