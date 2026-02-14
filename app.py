from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def game():
    result = None
    user_choice = None
    computer_choice = None

    if request.method == "POST":
        user_choice = request.form.get("choice")
        options = ["rock", "paper", "scissors"]
        computer_choice = random.choice(options)

        if user_choice == computer_choice:
            result = "Draw"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
                (user_choice == "paper" and computer_choice == "rock") or \
                (user_choice == "scissors" and computer_choice == "paper"):
            result = "You win!"
        else:
            result = "You lose!"

    return render_template("index.html", result=result, user=user_choice, computer=computer_choice)

if __name__ == "__main__":
    app.run(debug=True)