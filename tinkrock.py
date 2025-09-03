import tkinter as tk
from tkinter import messagebox
import random
class RockPaperScissorsGame:
    def init(self, master):
        self.master = master
        master.title("Rock, Paper, Scissors")
        master.geometry("400x350")
        master.resizable(False, False)
        master.configure(bg="#e0e0e0")
        self.user_score = 0
        self.computer_score = 0
        self.choices = ["rock", "paper", "scissors"]

        self.create_widgets()

def create_widgets(self):
    """
    Creates and places all the GUI widgets for the game.
    """
    # Title Label
    self.title_label = tk.Label(
        self.master,
        text="Rock, Paper, Scissors!",
        font=("Arial", 20, "bold"),
        bg="#e0e0e0",
        fg="#333333"
    )
    self.title_label.pack(pady=10)

    # Score Labels
    self.score_frame = tk.Frame(self.master, bg="#e0e0e0")
    self.score_frame.pack(pady=5)

    self.user_score_label = tk.Label(
        self.score_frame,
        text=f"You: {self.user_score}",
        font=("Arial", 14),
        bg="#e0e0e0",
        fg="#006600"
    )
    self.user_score_label.pack(side=tk.LEFT, padx=20)

    self.computer_score_label = tk.Label(
        self.score_frame,
        text=f"Computer: {self.computer_score}",
        font=("Arial", 14),
        bg="#e0e0e0",
        fg="#cc0000"
    )
    self.computer_score_label.pack(side=tk.RIGHT, padx=20)

    # Result Label
    self.result_label = tk.Label(
        self.master,
        text="Make your move!",
        font=("Arial", 16),
        bg="#e0e0e0",
        fg="#444444"
    )
    self.result_label.pack(pady=15)

    # Buttons for user choices
    self.button_frame = tk.Frame(self.master, bg="#e0e0e0")
    self.button_frame.pack(pady=10)

    self.rock_button = tk.Button(
        self.button_frame,
        text="Rock",
        command=lambda: self.play_game("rock"),
        font=("Arial", 12, "bold"),
        width=10,
        bg="#6a0572",
        fg="white",
        activebackground="#8a2be2"
    )
    self.rock_button.grid(row=0, column=0, padx=5, pady=5)

    self.paper_button = tk.Button(
        self.button_frame,
        text="Paper",
        command=lambda: self.play_game("paper"),
        font=("Arial", 12, "bold"),
        width=10,
        bg="#2e8b57",
        fg="white",
        activebackground="#3cb371"
    )
    self.paper_button.grid(row=0, column=1, padx=5, pady=5)

    self.scissors_button = tk.Button(
        self.button_frame,
        text="Scissors",
        command=lambda: self.play_game("scissors"),
        font=("Arial", 12, "bold"),
        width=10,
        bg="#b22222",
        fg="white",
        activebackground="#dc143c"
    )
    self.scissors_button.grid(row=0, column=2, padx=5, pady=5)

    # Reset Button
    self.reset_button = tk.Button(
        self.master,
        text="Reset Game",
        command=self.reset_game,
        font=("Arial", 12),
        bg="#f0ad4e",
        fg="white",
        activebackground="#ec971f"
    )
    self.reset_button.pack(pady=15)

def play_game(self, user_choice):
    """
    Contains the game logic for a single round of Rock, Paper, Scissors.
    """
    computer_choice = random.choice(self.choices)
    result_text = f"You chose: {user_choice.capitalize()}\nComputer chose: {computer_choice.capitalize()}\n"
    
    if user_choice == computer_choice:
        result_text += "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        result_text += "You win this round!"
        self.user_score += 1
    else:
        result_text += "Computer wins this round!"
        self.computer_score += 1

    self.result_label.config(text=result_text)
    self.update_score_labels()

def update_score_labels(self):
    """
    Updates the score display on the GUI.
    """
    self.user_score_label.config(text=f"You: {self.user_score}")
    self.computer_score_label.config(text=f"Computer: {self.computer_score}")

def reset_game(self):
    """
    Resets the game scores and result display.
    """
    self.user_score = 0
    self.computer_score = 0
    self.update_score_labels()
    self.result_label.config(text="Game reset! Make your move!")
    messagebox.showinfo("Game Reset", "The game has been reset!")