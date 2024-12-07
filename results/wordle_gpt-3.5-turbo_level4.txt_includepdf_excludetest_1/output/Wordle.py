"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():
    def enter_action(s):
        # Check if the entered word is in the word list
        if s.lower() in FIVE_LETTER_WORDS:
            # Display a positive message
            gw.show_message("Good job! You found a word!")
        else:
            # Display a message indicating the word is not in the list
            gw.show_message("Not in word list", color="red")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()