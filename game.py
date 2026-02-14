import random

def play_game():
    """
    Play a game of Rock, Paper, Scissors
    """

    player_wins = 0
    computer_wins = 0
    choices = ['rock', 'paper', 'scissors']

    print("Welcome to Rock, Paper, Scissors")

    while True:
        # Get the players input
        player = input("Make your choice(rock, paper, scissors): or 'quit' to end:")
        if player =='quit':
            break
        if player not in choices:
            print("Invalid choice, please try again")
            continue

        # Get computer choice
        computer = random.choice(choices)
        print(f"\nYou choice{player}, computer choice{computer}.")

        # Determine the winner
        if player == computer:
            print(f"Both players selected {player}. It is a tie!")
        elif (player == "rock" and computer == "scissors") or \
                (player == "paper" and computer == "rock") or \
                (player == "scissors" and computer == "paper"):
            print(f"{player.capitalize()} beats {computer}. You win!")
            player_wins += 1
        else:
            print(f"{computer.capitalize()} beats {player}. You lose.")
            computer_wins += 1

        print(f"Score: You have {player_wins} wins, Computer has {computer_wins} wins\n")

    print("Thanks for playing")
    print(f"Final Score: You:{player_wins}, Computer:{computer_wins}")

# Run the game
if __name__ == "__main__":
    play_game()
