"""
This module is the main entry point for the Wordle assignment.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():
    def enter_action(s):
        # Implementing the enter action method
        if s.lower() in FIVE_LETTER_WORDS:
            # Check if the entered word is in the dictionary
            gw.show_message("Correct guess!")
        else:
            gw.show_message("Not in word list")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()