# Your implementation of the Wordle game goes here

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():
    def enter_action(s):
        if s.lower() in FIVE_LETTER_WORDS:
            word = FIVE_LETTER_WORDS[random.randint(0, len(FIVE_LETTER_WORDS) - 1)].upper()
            for i in range(5):
                gw.set_square_letter(0, i, word[i])
            if s.upper() == word:
                gw.show_message("Congratulations! You guessed the word correctly!", "Green")
            else:
                check_word(s.upper(), word)
        else:
            gw.show_message("Not in word list", "Red")

    def check_word(guess, target):
        for i, letter in enumerate(guess):
            if letter == target[i]:
                gw.set_square_color(gw.get_current_row(), i, "#66BB66")  # Correct color
            elif letter in target:
                gw.set_square_color(gw.get_current_row(), i, "#CCBB66")  # Present color
            else:
                gw.set_square_color(gw.get_current_row(), i, "#999999")  # Missing color

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

if __name__ == "__main__":
    wordle()