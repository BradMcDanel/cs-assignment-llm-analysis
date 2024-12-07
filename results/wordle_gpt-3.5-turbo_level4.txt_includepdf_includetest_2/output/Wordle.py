import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():
    def enter_action(s):
        pass

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

if __name__ == "__main__":
    wordle()