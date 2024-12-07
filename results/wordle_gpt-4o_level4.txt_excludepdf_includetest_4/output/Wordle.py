"""
This module is the implementation file for the Wordle assignment.
"""

import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, N_ROWS, N_COLS

def wordle():
    # Pick a random word from the dictionary
    target_word = random.choice(FIVE_LETTER_WORDS).upper()

    # Initialize the graphics window
    gw = WordleGWindow()

    # Function to handle the enter key action
    def enter_action(s):
        current_row = gw.get_current_row()
        guess = s.strip().upper()

        # Check if the guess is a valid word
        if guess.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return

        # Color the squares based on the guess
        target_word_list = list(target_word)
        guess_list = list(guess)

        # First pass: mark correct letters
        for col in range(N_COLS):
            if guess_list[col] == target_word_list[col]:
                gw.set_square_color(current_row, col, CORRECT_COLOR)
                gw.set_key_color(guess_list[col], CORRECT_COLOR)
                target_word_list[col] = None  # Mark this letter as used
                guess_list[col] = None

        # Second pass: mark present letters
        for col in range(N_COLS):
            if guess_list[col] is not None and guess_list[col] in target_word_list:
                gw.set_square_color(current_row, col, PRESENT_COLOR)
                gw.set_key_color(guess_list[col], PRESENT_COLOR)
                target_word_list[target_word_list.index(guess_list[col])] = None  # Mark this letter as used
            elif guess_list[col] is not None:
                gw.set_square_color(current_row, col, MISSING_COLOR)
                gw.set_key_color(guess_list[col], MISSING_COLOR)

        # Check if the guess was correct
        if guess == target_word:
            gw.show_message("Congratulations! You've guessed the word!")
        elif current_row == N_ROWS - 1:
            gw.show_message(f"You've used all your guesses. The word was {target_word}.")
        else:
            gw.set_current_row(current_row + 1)

    # Add the listener for enter action
    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()