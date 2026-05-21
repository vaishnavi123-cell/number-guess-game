import tkinter as tk
from tkinter import messagebox
import random

# Random number generate
number = random.randint(1, 100)

# Attempt counter
attempts = 0


# Function to check guess
def check_guess():
    global attempts

    guess = entry.get()

    # Empty check
    if guess == "":
        messagebox.showwarning("Warning", "Please enter a number")
        return

    guess = int(guess)
    attempts += 1

    if guess < number:
        result_label.config(text="Too Low 🔻")

    elif guess > number:
        result_label.config(text="Too High 🔺")

    else:
        result_label.config(
            text=f"Correct! 🎉 You guessed in {attempts} attempts"
        )


# GUI Window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x300")
root.config(bg="lightblue")

# Title
title_label = tk.Label(
    root,
    text="Guess The Number (1-100)",
    font=("Arial", 16, "bold"),
    bg="lightblue"
)
title_label.pack(pady=20)

# Entry Box
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

# Button
guess_button = tk.Button(
    root,
    text="Check",
    font=("Arial", 12),
    command=check_guess
)
guess_button.pack(pady=10)

# Result Label
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 14),
    bg="lightblue"
)
result_label.pack(pady=20)

# Run window
root.mainloop()