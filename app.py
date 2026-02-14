from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = "super_secret_key_2026" # Required for sessions

@app.route("/", methods=["GET", "POST"])
def game():
    # Initialize scores if they don't exist
    if "user_score" not in session:
        session["user_score"] = 0
        session["cpu_score"] = 0

    result, user_choice, cpu_choice = None, None, None
    game_over = False

    if request.method == "POST":
        user_choice = request.form.get("choice")
        options = ["rock", "paper", "scissors"]
        cpu_choice = random.choice(options)

        # Determine winner
        if user_choice == cpu_choice:
            result = "Tie"
        elif (user_choice == "rock" and cpu_choice == "scissors") or \
             (user_choice == "paper" and cpu_choice == "rock") or \
             (user_choice == "scissors" and cpu_choice == "paper"):
            result = "Win"
            session["user_score"] += 1
        else:
            result = "Lose"
            session["cpu_score"] += 1

        # Check for Final Game Over (e.g., first to 3)
        if session["user_score"] >= 3 or session["cpu_score"] >= 3:
            game_over = True

    return render_template("index.html", result=result, user=user_choice,
                           cpu=cpu_choice, user_score=session["user_score"],
                           cpu_score=session["cpu_score"], game_over=game_over)

@app.route("/reset")
def reset():
    session.clear()
    return redirect(url_for("game"))

if __name__ == "__main__":
    app.run(debug=True)