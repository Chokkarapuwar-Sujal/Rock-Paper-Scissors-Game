import tkinter as tk
import random

# Initialize main window
root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.geometry("420x450")
root.resizable(False, False)

# Global score variables
player_score = 0
computer_score = 0

# Variables for tracking state
player_choice = ""
computer_choice = ""

# Determine winner
def get_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

# Reset labels and start new round
def play(choice):
    global player_choice
    player_choice = choice
    status_label.config(text="Your Turn...")
    player_label.config(text="")
    computer_label.config(text="")
    result_label.config(text="")
    root.after(500, show_player_choice)

def show_player_choice():
    player_label.config(text=f"You chose: {player_choice}")
    status_label.config(text="Computer's Turn...")
    root.after(1000, computer_turn)

def computer_turn():
    global computer_choice, player_score, computer_score
    computer_choice = random.choice(["rock", "paper", "scissors"])
    computer_label.config(text=f"Computer chose: {computer_choice}")
    
    result = get_winner(player_choice, computer_choice)
    result_label.config(text=result)

    if result == "You win!":
        player_score += 1
    elif result == "Computer wins!":
        computer_score += 1

    player_score_label.config(text=f"Player Score: {player_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")
    status_label.config(text="Play again!")

# Reset the entire game
def reset_game():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    player_score_label.config(text="Player Score: 0")
    computer_score_label.config(text="Computer Score: 0")
    player_label.config(text="")
    computer_label.config(text="")
    result_label.config(text="")
    status_label.config(text="Choose Rock, Paper, or Scissors to start!")

# Title
title = tk.Label(root, text="Rock - Paper - Scissors", font=('Arial', 16, 'bold'))
title.pack(pady=10)

# Scoreboard
score_frame = tk.Frame(root)
score_frame.pack()

player_score_label = tk.Label(score_frame, text="Player Score: 0", font=('Arial', 12))
player_score_label.grid(row=0, column=0, padx=20)

computer_score_label = tk.Label(score_frame, text="Computer Score: 0", font=('Arial', 12))
computer_score_label.grid(row=0, column=1, padx=20)

# Game status label
status_label = tk.Label(root, text="Choose Rock, Paper, or Scissors to start!", font=('Arial', 12, 'italic'), fg="blue")
status_label.pack(pady=10)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

rock_btn = tk.Button(button_frame, text="Rock", width=12, command=lambda: play("rock"))
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(button_frame, text="Paper", width=12, command=lambda: play("paper"))
paper_btn.grid(row=0, column=1, padx=5)

scissors_btn = tk.Button(button_frame, text="Scissors", width=12, command=lambda: play("scissors"))
scissors_btn.grid(row=0, column=2, padx=5)

# Result display
player_label = tk.Label(root, text="", font=('Arial', 12))
player_label.pack(pady=5)

computer_label = tk.Label(root, text="", font=('Arial', 12))
computer_label.pack(pady=5)

result_label = tk.Label(root, text="", font=('Arial', 14, 'bold'))
result_label.pack(pady=10)

# Reset button
reset_button = tk.Button(root, text="Reset Game", width=15, command=reset_game)
reset_button.pack(pady=10)

# Run app
root.mainloop()
