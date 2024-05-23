"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    def pick_random_word():
        return random.choice(FIVE_LETTER_WORDS).upper()

    def display_word(word):
        for col in range(N_COLS):
            gw.set_square_letter(0, col, word[col])

    def enter_action(s):
        current_row = gw.get_current_row()
        if s.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return

        for col in range(N_COLS):
            letter = s[col]
            if letter == hidden_word[col]:
                gw.set_square_color(current_row, col, CORRECT_COLOR)
            elif letter in hidden_word:
                gw.set_square_color(current_row, col, PRESENT_COLOR)
            else:
                gw.set_square_color(current_row, col, MISSING_COLOR)

        if s == hidden_word:
            gw.show_message("Congratulations! You've guessed the word!")
        elif current_row == N_ROWS - 1:
            gw.show_message(f"Game over! The word was {hidden_word}.")
        else:
            gw.set_current_row(current_row + 1)

    hidden_word = pick_random_word()
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
    display_word(hidden_word)

# Startup code
if __name__ == "__main__":
    wordle()