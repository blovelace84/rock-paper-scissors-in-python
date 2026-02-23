from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = "secretkey123"

choices = ["rock", "paper", "scissors"]

def get_winner(player, computer):
    if player == computer:
        return "Tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "You Win!"
    else:
        return "Computer Wins!"

@app.route("/", methods=["GET", "POST"])
def index():
    if "player_score" not in session:
        session["player_score"] = 0
        session["computer_score"] = 0

    result = ""
    computer_choice = ""

    if request.method == "POST":
        player_choice = request.form["choice"]
        computer_choice = random.choice(choices)

        result = get_winner(player_choice, computer_choice)

        if result == "You Win!":
            session["player_score"] += 1
        elif result == "Computer Wins!":
            session["computer_score"] += 1

    return render_template(
        "index.html",
        result=result,
        computer_choice=computer_choice,
        player_score=session["player_score"],
        computer_score=session["computer_score"]
    )

if __name__ == "__main__":
    app.run(debug=True)