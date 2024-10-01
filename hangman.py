import random
import tkinter as tk
from tkinter import messagebox
HANGMAN = [
    """
    ------
    |    |
    |
    |
    |
    |
    |
    |
    |
    ----------
    """,
    """
    ------
    |    |
    |    O
    |
    |
    |
    |
    |
    |
    ----------
    """,
    """
    ------
    |    |
    |    O
    |   -+-
    | 
    |   
    |   
    |   
    |   
    ----------
    """,
    """
    ------
    |    |
    |    O
    |  /-+-
    |   
    |   
    |   
    |   
    |   
    ----------
    """,
    """
    ------
    |    |
    |    O
    |  /-+-/
    |   
    |   
    |   
    |   
    |   
    ----------
    """,
    """
    ------
    |    |
    |    O
    |  /-+-/
    |    |
    |   
    |   
    |   
    |   
    ----------
    """,
    """
    ------
    |    |
    |    O
    |  /-+-/
    |    |
    |    |
    |   | 
    |   | 
    |   
    ----------
    """,
    """
    ------
    |    |
    |    O
    |  /-+-/
    |    |
    |    |
    |   | |
    |   | |
    |  
    ----------
    """
]

WORDS = ["THE GRIND", "HANGMAN", "WHEEL OF FORTUNE", "AEROPOSTALE", 
         "PYTHON", "CASABLANCA", "ALASKA", "SILLY GOOSE", "OVERUSED"]

MAX_WRONG = len(HANGMAN) - 1

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        
    
        self.word = random.choice(WORDS).upper()
        self.so_far = "-" * len(self.word)
        self.wrong = 0
        self.used = []

        self.hangman_label = tk.Label(root, text=HANGMAN[self.wrong], font=("Courier", 12), justify='left')
        self.hangman_label.pack()

        self.so_far_label = tk.Label(root, text=self.so_far, font=("Courier", 16))
        self.so_far_label.pack()

        self.guess_entry = tk.Entry(root, font=("Courier", 14))
        self.guess_entry.pack()

        
        self.guess_button = tk.Button(root, text="Guess", command=self.make_guess, font=("Courier", 14))
        self.guess_button.pack()

        self.used_label = tk.Label(root, text="Used letters: ", font=("Courier", 12))
        self.used_label.pack()

    def make_guess(self):
        guess = self.guess_entry.get().upper()
        self.guess_entry.delete(0, tk.END)

        if not guess or len(guess) != 1 or not guess.isalpha():
            messagebox.showwarning("Invalid input", "Please enter a single letter.")
            return

        if guess in self.used:
            messagebox.showwarning("Already used", f"You already guessed {guess}")
            return

        self.used.append(guess)
        self.used_label.config(text=f"Used letters: {', '.join(self.used)}")

        if guess in self.word:
            self.update_so_far(guess)
        else:
            self.wrong += 1
            self.hangman_label.config(text=HANGMAN[self.wrong])

        if self.wrong == MAX_WRONG:
            messagebox.showinfo("Game Over", f"You've been hanged! The word was: {self.word}")
            self.root.quit()
        elif self.so_far == self.word:
            messagebox.showinfo("Congratulations!", "You guessed the word!")
            self.root.quit()

    def update_so_far(self, guess):
        new = ""
        for i in range(len(self.word)):
            if self.word[i] == guess:
                new += guess
            else:
                new += self.so_far[i]
        self.so_far = new
        self.so_far_label.config(text=self.so_far)



root = tk.Tk()
game = HangmanGame(root)
root.mainloop()
