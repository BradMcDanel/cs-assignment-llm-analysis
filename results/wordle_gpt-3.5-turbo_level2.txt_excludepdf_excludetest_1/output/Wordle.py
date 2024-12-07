""" 
This module is the starter file for the Wordle assignment.
"""
import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow

def wordle():
    def enter_action(s):
        if s.lower() in FIVE_LETTER_WORDS:
            gw.show_message("Congratulations! Correct word.")
            check_word(s.lower())
        else:
            gw.show_message("Not in word list")

    def check_word(s):
        hidden_word = FIVE_LETTER_WORDS[random.randint(0, len(FIVE_LETTER_WORDS)-1)]
        for i in range(len(s)):
            if s[i] == hidden_word[i]:
                gw.set_square_color(0, i, WordleGWindow.CORRECT_COLOR)
            elif s[i] in hidden_word:
                gw.set_square_color(0, i, WordleGWindow.PRESENT_COLOR)
            else:
                gw.set_square_color(0, i, WordleGWindow.MISSING_COLOR)

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

if __name__ == "__main__":
    wordle()