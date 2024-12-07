# File: Wordle.py

"""
This module implements the Wordle game using the WordleGraphics module for display.
"""

import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    def enter_action(s):
        nonlocal guess_count
        s = s.lower()
        if s not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return
        
        guess_count += 1
        color_guess(s)
        
        if s == hidden_word:
            gw.show_message("Congratulations!")
        elif guess_count == N_ROWS:
            gw.show_message(f"The word was {hidden_word}")
        else:
            gw.set_current_row(guess_count)

    def color_guess(guess):
        word_letters = list(hidden_word)
        for col in range(N_COLS):
            letter = guess[col]
            if letter == hidden_word[col]:
                color = CORRECT_COLOR
                word_letters[col] = None
            elif letter in word_letters:
                color = PRESENT_COLOR
                word_letters[word_letters.index(letter)] = None
            else:
                color = MISSING_COLOR
            
            gw.set_square_color(guess_count, col, color)
            update_key_color(letter, color)

    def update_key_color(letter, color):
        current_color = gw.get_key_color(letter.upper())
        if current_color == CORRECT_COLOR:
            return
        if current_color == PRESENT_COLOR and color != CORRECT_COLOR:
            return
        gw.set_key_color(letter.upper(), color)

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    hidden_word = random.choice(FIVE_LETTER_WORDS)
    guess_count = 0

# Startup code

if __name__ == "__main__":
    wordle()