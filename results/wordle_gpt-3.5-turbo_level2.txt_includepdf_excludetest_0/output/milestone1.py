# Milestone #1: Pick a random word and display it in the first row of boxes

import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS

def milestone1():
    word = random.choice(FIVE_LETTER_WORDS)
    gw = WordleGWindow()
    for col, letter in enumerate(word):
        gw.set_square_letter(0, col, letter)

# Startup code
if __name__ == "__main__":
    milestone1()