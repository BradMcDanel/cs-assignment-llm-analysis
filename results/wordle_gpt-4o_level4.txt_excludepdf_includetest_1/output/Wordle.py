"""
This module is the complete implementation for the Wordle assignment.
"""

import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, N_ROWS, N_COLS

def wordle():
    # Select a random word from the dictionary
    secret_word = random.choice(FIVE_LETTER_WORDS).upper()

    def enter_action(guess):
        guess = guess.upper()

        # Check if the guess is a valid word
        if guess.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return

        current_row = gw.get_current_row()

        # Check and color the letters
        secret_word_copy = list(secret_word)
        colors = [MISSING_COLOR] * N_COLS

        # First pass: check for correct letters (green)
        for i in range(N_COLS):
            if guess[i] == secret_word[i]:
                colors[i] = CORRECT_COLOR
                secret_word_copy[i] = None  # Mark this letter as used

        # Second pass: check for present letters (yellow)
        for i in range(N_COLS):
            if colors[i] == MISSING_COLOR and guess[i] in secret_word_copy:
                colors[i] = PRESENT_COLOR
                secret_word_copy[secret_word_copy.index(guess[i])] = None  # Mark this letter as used

        # Update the graphics
        for i in range(N_COLS):
            gw.set_square_letter(current_row, i, guess[i])
            gw.set_square_color(current_row, i, colors[i])
            gw.set_key_color(guess[i], colors[i])

        # Check if the game is won
        if guess == secret_word:
            gw.show_message("Congratulations! You've guessed the word!")
        elif current_row == N_ROWS - 1:
            gw.show_message(f"Game over! The word was {secret_word}.")
        else:
            gw.set_current_row(current_row + 1)

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()