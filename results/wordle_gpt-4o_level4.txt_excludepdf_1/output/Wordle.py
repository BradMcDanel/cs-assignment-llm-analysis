"""
This module is the implementation file for the Wordle assignment.
"""

import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, N_ROWS, N_COLS

def wordle():
    def enter_action(s):
        current_row = gw.get_current_row()
        guess = ""
        
        for col in range(N_COLS):
            guess += gw.get_square_letter(current_row, col)
        
        if guess.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return

        for col in range(N_COLS):
            if guess[col] == secret_word[col]:
                gw.set_square_color(current_row, col, CORRECT_COLOR)
                gw.set_key_color(guess[col], CORRECT_COLOR)
            elif guess[col] in secret_word:
                gw.set_square_color(current_row, col, PRESENT_COLOR)
                if gw.get_key_color(guess[col]) != CORRECT_COLOR:
                    gw.set_key_color(guess[col], PRESENT_COLOR)
            else:
                gw.set_square_color(current_row, col, MISSING_COLOR)
                if gw.get_key_color(guess[col]) != CORRECT_COLOR and gw.get_key_color(guess[col]) != PRESENT_COLOR:
                    gw.set_key_color(guess[col], MISSING_COLOR)
        
        if guess == secret_word:
            gw.show_message("Congratulations! You found the word!")
            return
        
        if current_row == N_ROWS - 1:
            gw.show_message(f"The word was: {secret_word.upper()}")
        else:
            gw.set_current_row(current_row + 1)

    # Initialize the graphics window
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    # Milestone 1: Pick a random word and display it in the first row of boxes
    secret_word = random.choice(FIVE_LETTER_WORDS)
    
    # Uncomment the following line if you want to cheat and know the word
    # print(f"Secret word: {secret_word}")

# Startup code
if __name__ == "__main__":
    wordle()