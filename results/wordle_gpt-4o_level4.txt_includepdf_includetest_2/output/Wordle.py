"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    # Pick a random word from the list
    target_word = random.choice(FIVE_LETTER_WORDS).upper()
    
    def enter_action(s):
        # Get the current row
        row = gw.get_current_row()

        # Check if the word is valid
        if s.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return

        # Check each letter and color the boxes
        guessed_correctly = True
        for i in range(N_COLS):
            letter = s[i]
            if letter == target_word[i]:
                gw.set_square_color(row, i, CORRECT_COLOR)
            elif letter in target_word:
                gw.set_square_color(row, i, PRESENT_COLOR)
                guessed_correctly = False
            else:
                gw.set_square_color(row, i, MISSING_COLOR)
                guessed_correctly = False

        # Check if the whole word was guessed correctly
        if guessed_correctly:
            gw.show_message("Congratulations! You've guessed the word!")
        else:
            gw.set_current_row(row + 1)
            if row + 1 == N_ROWS:
                gw.show_message(f"Game Over! The word was {target_word}")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()