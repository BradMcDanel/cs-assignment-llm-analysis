import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():

    def enter_action(s):
        word = FIVE_LETTER_WORDS[random.randint(0, len(FIVE_LETTER_WORDS) - 1)]
        if s.upper() == word.upper():
            gw.show_message("Congratulations! You guessed the word correctly.")
            for col in range(N_COLS):
                gw.set_square_color(gw.get_current_row(), col, "#66BB66")  # Set correct color for all squares
        else:
            gw.show_message("Not in word list")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code

if __name__ == "__main__":
    wordle()