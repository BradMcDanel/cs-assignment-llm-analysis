# Milestone #2: Check whether the letters entered by the user form a word
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS

def milestone2():
    def enter_action(s):
        if s.lower() in FIVE_LETTER_WORDS:
            gw.show_message("Word is in word list")
        else:
            gw.show_message("Not in word list")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

if __name__ == "__main__":
    milestone2()