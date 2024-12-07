from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def is_valid_word(word):
    return word in FIVE_LETTER_WORDS

def enter_action(s):
    if not is_valid_word(s):
        gw.show_message("Not in word list")
    else:
        gw.show_message("Valid word entered")

def wordle():
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

if __name__ == "__main__":
    wordle()