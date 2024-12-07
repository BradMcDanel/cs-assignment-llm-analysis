import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():
    def enter_action(s):
        if s.lower() == target_word:
            gw.show_message("Congratulations! You guessed the word.")
            for i in range(N_COLS):
                gw.set_square_color(0, i, CORRECT_COLOR)
        else:
            gw.show_message("Not in word list")

    target_word = random.choice(FIVE_LETTER_WORDS)
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

if __name__ == "__main__":
    wordle()