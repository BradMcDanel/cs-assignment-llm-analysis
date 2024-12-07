import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def milestone3():
    gw = WordleGWindow()
    def enter_action(s):
        if s.lower() in FIVE_LETTER_WORDS:
            # Implement coloring of boxes based on correct letters
            gw.show_message("Word found!")
        else:
            gw.show_message("Not in word list")

    gw.add_enter_listener(enter_action)

if __name__ == "__main__":
    milestone3()