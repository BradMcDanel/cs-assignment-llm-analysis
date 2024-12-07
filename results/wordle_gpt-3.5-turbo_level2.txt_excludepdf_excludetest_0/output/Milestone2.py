from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow

def enter_action(word):
    if word.lower() in FIVE_LETTER_WORDS:
        gw.show_message("Word is in word list.")
    else:
        gw.show_message("Not in word list")

gw = WordleGWindow()
gw.add_enter_listener(enter_action)