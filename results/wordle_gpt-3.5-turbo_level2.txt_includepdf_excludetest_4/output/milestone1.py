# Milestone #1: Pick a random word and display it in the first row of boxes

import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def milestone1():
    word = random.choice(FIVE_LETTER_WORDS)
    gw = WordleGWindow()
    for i in range(N_COLS):
        gw.set_square_letter(0, i, word[i])

if __name__ == "__main__":
    milestone1()