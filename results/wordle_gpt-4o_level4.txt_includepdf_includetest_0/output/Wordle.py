"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    target_word = random.choice(FIVE_LETTER_WORDS).upper()
    current_row = 0

    def enter_action(guess):
        nonlocal current_row
        guess = guess.upper()

        if guess not in map(str.upper, FIVE_LETTER_WORDS):
            gw.show_message("Not in word list")
            return

        for col in range(N_COLS):
            gw.set_square_letter(current_row, col, guess[col])

        target_letter_count = {letter: target_word.count(letter) for letter in set(target_word)}

        for col in range(N_COLS):
            if guess[col] == target_word[col]:
                gw.set_square_color(current_row, col, CORRECT_COLOR)
                gw.set_key_color(guess[col], CORRECT_COLOR)
                target_letter_count[guess[col]] -= 1
            else:
                gw.set_square_color(current_row, col, MISSING_COLOR)

        for col in range(N_COLS):
            if guess[col] != target_word[col] and guess[col] in target_word and target_letter_count[guess[col]] > 0:
                gw.set_square_color(current_row, col, PRESENT_COLOR)
                gw.set_key_color(guess[col], PRESENT_COLOR)
                target_letter_count[guess[col]] -= 1
            elif guess[col] != target_word[col]:
                gw.set_key_color(guess[col], MISSING_COLOR)

        if guess == target_word:
            gw.show_message("Congratulations! You've guessed the word!")
        elif current_row == N_ROWS - 1:
            gw.show_message(f"Game Over! The word was {target_word}.")
        else:
            current_row += 1
            gw.set_current_row(current_row)

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code

if __name__ == "__main__":
    wordle()