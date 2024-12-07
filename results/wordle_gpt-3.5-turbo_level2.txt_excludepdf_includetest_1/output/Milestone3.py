from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def enter_action(s):
    if s.lower() in FIVE_LETTER_WORDS:
        # Logic to color the boxes based on correct, present, or missing letters
        pass
    else:
        gw.show_message("Not in word list")

def milestone3():
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

if __name__ == "__main__":
    milestone3()