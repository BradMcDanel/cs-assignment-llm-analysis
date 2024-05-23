# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    # Milestone #1: Pick a random word
    secret_word = random.choice(FIVE_LETTER_WORDS).upper()

    def enter_action(s):
        current_row = gw.get_current_row()
        guess = s.upper()

        # Milestone #2: Check if the guess is a valid word
        if guess.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return
        
        # Milestone #3: Color the boxes based on the guess
        letter_count = {}
        for letter in secret_word:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
        
        for i, letter in enumerate(guess):
            if letter == secret_word[i]:
                gw.set_square_color(current_row, i, CORRECT_COLOR)
                letter_count[letter] -= 1
            else:
                gw.set_square_color(current_row, i, MISSING_COLOR)

        for i, letter in enumerate(guess):
            if gw.get_square_color(current_row, i) != CORRECT_COLOR:
                if letter in secret_word and letter_count[letter] > 0:
                    gw.set_square_color(current_row, i, PRESENT_COLOR)
                    letter_count[letter] -= 1
                else:
                    gw.set_square_color(current_row, i, MISSING_COLOR)
        
        # Milestone #4: Color the keys
        for letter in guess:
            if letter in secret_word:
                if secret_word.count(letter) == guess.count(letter):
                    gw.set_key_color(letter, CORRECT_COLOR)
                else:
                    gw.set_key_color(letter, PRESENT_COLOR)
            else:
                gw.set_key_color(letter, MISSING_COLOR)

        # Check if the guess is correct
        if guess == secret_word:
            gw.show_message("Congratulations!")
        elif current_row == N_ROWS - 1:
            gw.show_message(f"The word was {secret_word}")
        else:
            gw.set_current_row(current_row + 1)

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()