from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow

def wordle():
    def enter_action(s):
        if s not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
        else:
            # Display positive message
            gw.show_message("Valid word!")

            # More logic to be added for coloring squares

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()