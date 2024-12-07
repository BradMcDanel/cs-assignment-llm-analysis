from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow

def milestone2(gw):
    def enter_action(s):
        is_valid_word = s.lower() in FIVE_LETTER_WORDS
        if is_valid_word:
            gw.show_message("Valid word!")
        else:
            gw.show_message("Not in word list")

    gw.add_enter_listener(enter_action)

gw = WordleGWindow()
milestone2(gw)