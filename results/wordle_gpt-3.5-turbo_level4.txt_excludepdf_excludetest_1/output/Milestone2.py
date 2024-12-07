from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow

def milestone2():
    def enter_action(s):
        # Check if the entered word is a legitimate English word
        if s.lower() in FIVE_LETTER_WORDS:
            # Show positive message
            gw.show_message("Congratulations! That's a correct word.")
            # Color the boxes to show matching letters (Milestone #3)
        else:
            # Show message for word not in the word list
            gw.show_message("Not in word list")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

if __name__ == "__main__":
    milestone2()