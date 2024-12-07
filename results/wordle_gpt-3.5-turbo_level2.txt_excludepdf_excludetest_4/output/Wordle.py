import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow

def wordle():
    
    def enter_action(s):
        if s.lower() in FIVE_LETTER_WORDS:
            # Check if the entered word is a valid 5-letter word
            gw.show_message("Valid word entered!")
            # Implement coloring logic for the squares
            # Update the key colors as well
            # Check if all letters match in correct position for victory
        else:
            gw.show_message("Not in word list")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

if __name__ == "__main__":
    wordle()