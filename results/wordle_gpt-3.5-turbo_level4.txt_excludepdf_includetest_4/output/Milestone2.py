from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow

def enter_action(s):
    if s.lower() in FIVE_LETTER_WORDS:
        gw.show_message("Valid word!")
    else:
        gw.show_message("Not in word list")

if __name__ == "__main__":
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)