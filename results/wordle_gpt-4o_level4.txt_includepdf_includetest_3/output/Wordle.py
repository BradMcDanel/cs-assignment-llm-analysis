"""
This module is the implementation for the Wordle assignment.
"""

import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    # Choose a random word from the dictionary
    target_word = random.choice(FIVE_LETTER_WORDS).upper()
    gw = WordleGWindow()

    def enter_action(s):
        current_row = gw.get_current_row()
        if s.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return

        # Check each letter and color the boxes
        target_word_list = list(target_word)
        guess_list = list(s)
        colors = [MISSING_COLOR] * N_COLS
        
        # First pass: check for correct positions
        for i in range(N_COLS):
            if guess_list[i] == target_word_list[i]:
                colors[i] = CORRECT_COLOR
                target_word_list[i] = None  # Mark this letter as used

        # Second pass: check for present letters
        for i in range(N_COLS):
            if colors[i] != CORRECT_COLOR and guess_list[i] in target_word_list:
                colors[i] = PRESENT_COLOR
                target_word_list[target_word_list.index(guess_list[i])] = None

        # Update the squares and keys
        for i in range(N_COLS):
            gw.set_square_color(current_row, i, colors[i])
            gw.set_key_color(guess_list[i], colors[i])

        # Check if the guess is correct
        if all(color == CORRECT_COLOR for color in colors):
            gw.show_message("Congratulations!")
        else:
            next_row = current_row + 1
            if next_row < N_ROWS:
                gw.set_current_row(next_row)
            else:
                gw.show_message(f"Game over! The word was: {target_word}")

    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()