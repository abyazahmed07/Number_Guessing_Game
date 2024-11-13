import tkinter as tk
from tkinter import messagebox
import random

def check_guess():
    global attempts
    try:
        guess = int(entry_guess.get())
        if guess < 1 or guess > 100:
            messagebox.showwarning("Invalid Input", "Please enter a number between 1 and 100.")
            return
        attempts += 1
        if guess < secret_number:
            result_label.config(text="Too low! Try again.")
        elif guess > secret_number:
            result_label.config(text="Too high! Try again.")
        else:
            result_label.config(text=f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
            disable_game()
        attempts_label.config(text=f"Attempts: {attempts}/{max_attempts}")
        if attempts >= max_attempts and guess != secret_number:
            result_label.config(text=f"Game Over! The number was {secret_number}.")
            disable_game()
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer.")

def disable_game():
    entry_guess.config(state='disabled')
    guess_button.config(state='disabled')

def restart_game():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0
    entry_guess.config(state='normal')
    guess_button.config(state='normal')
    entry_guess.delete(0, tk.END)
    result_label.config(text="")
    attempts_label.config(text=f"Attempts: {attempts}/{max_attempts}")

root = tk.Tk()
root.title("Guess the Number Game")
root.geometry("400x300")

secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 10

instruction_label = tk.Label(root, text="Guess a number between 1 and 100:")
instruction_label.pack(pady=10)

entry_guess = tk.Entry(root)
entry_guess.pack(pady=5)

guess_button = tk.Button(root, text="Guess", command=check_guess)
guess_button.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

attempts_label = tk.Label(root, text=f"Attempts: {attempts}/{max_attempts}")
attempts_label.pack(pady=5)

restart_button = tk.Button(root, text="Restart Game", command=restart_game)
restart_button.pack(pady=10)

root.mainloop()