from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS

def wordle():

    def enter_action(s):
        gw.show_message("You have to implement this method.")
        if s.lower() in FIVE_LETTER_WORDS:
            gw.show_message("Valid word entered!")
        else:
            gw.show_message("Not in word list")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code

if __name__ == "__main__":
    wordle()