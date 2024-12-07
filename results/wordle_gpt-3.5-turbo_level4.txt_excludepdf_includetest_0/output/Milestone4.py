from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow

def milestone4():
    def enter_action(s):
        if s.lower() in FIVE_LETTER_WORDS:
            # Logic to color the boxes and keys
            pass
        else:
            gw.show_message("Not in word list")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

if __name__ == "__main__":
    milestone4()