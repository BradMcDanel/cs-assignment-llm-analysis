import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow

def wordle():
    def enter_action(s):
        if s.lower() in FIVE_LETTER_WORDS:
            # Check if the word is in the dictionary
            gw.show_message("Valid word entered.")
            # Add logic here to color the boxes based on the word entered
        else:
            gw.show_message("Not in word list.")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

if __name__ == "__main__":
    wordle()