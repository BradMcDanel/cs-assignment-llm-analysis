"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    secret_word = random.choice(FIVE_LETTER_WORDS).upper()
    current_row = 0

    def enter_action(s):
        nonlocal current_row
        guess = s.strip().upper()

        if len(guess) != N_COLS or guess.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return

        for col in range(N_COLS):
            letter = guess[col]
            if letter == secret_word[col]:
                gw.set_square_color(current_row, col, CORRECT_COLOR)
                gw.set_key_color(letter, CORRECT_COLOR)
            elif letter in secret_word:
                gw.set_square_color(current_row, col, PRESENT_COLOR)
                if gw.get_key_color(letter) != CORRECT_COLOR:
                    gw.set_key_color(letter, PRESENT_COLOR)
            else:
                gw.set_square_color(current_row, col, MISSING_COLOR)
                if gw.get_key_color(letter) not in [CORRECT_COLOR, PRESENT_COLOR]:
                    gw.set_key_color(letter, MISSING_COLOR)

        if guess == secret_word:
            gw.show_message("You guessed it!")
        else:
            current_row += 1
            if current_row == N_ROWS:
                gw.show_message(f"The word was {secret_word}")
            else:
                gw.set_current_row(current_row)

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()