"""
This module implements the Wordle game.
"""

import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    # Pick a random word from the list
    secret_word = random.choice(FIVE_LETTER_WORDS).upper()
    gw = WordleGWindow()

    def enter_action(guess):
        guess = guess.upper()
        current_row = gw.get_current_row()

        # Check if the guess is a valid word
        if guess.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return

        # Color the boxes based on the guess
        secret_word_letters = list(secret_word)
        guess_letters = list(guess)

        # First pass for correct positions
        for i in range(N_COLS):
            if guess_letters[i] == secret_word_letters[i]:
                gw.set_square_color(current_row, i, CORRECT_COLOR)
                gw.set_key_color(guess_letters[i], CORRECT_COLOR)
                secret_word_letters[i] = None
                guess_letters[i] = None

        # Second pass for present letters
        for i in range(N_COLS):
            if guess_letters[i] is not None and guess_letters[i] in secret_word_letters:
                gw.set_square_color(current_row, i, PRESENT_COLOR)
                if gw.get_key_color(guess_letters[i]) != CORRECT_COLOR:
                    gw.set_key_color(guess_letters[i], PRESENT_COLOR)
                secret_word_letters[secret_word_letters.index(guess_letters[i])] = None

        # Final pass for missing letters
        for i in range(N_COLS):
            if guess_letters[i] is not None:
                gw.set_square_color(current_row, i, MISSING_COLOR)
                if gw.get_key_color(guess_letters[i]) not in (CORRECT_COLOR, PRESENT_COLOR):
                    gw.set_key_color(guess_letters[i], MISSING_COLOR)

        # Check win condition
        if guess == secret_word:
            gw.show_message("Congratulations! You've guessed the word!")
        else:
            if current_row < N_ROWS - 1:
                gw.set_current_row(current_row + 1)
            else:
                gw.show_message(f"Game over! The word was {secret_word}.")

    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()