import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow

def wordle():
    def enter_action(s):
        # Check if the entered word is a valid English word
        if s.lower() in FIVE_LETTER_WORDS:
            # Display positive message
            gw.show_message("Valid English word!")
            # Color the boxes to show the user which letters in the guess match the word
            for i, char in enumerate(s):
                if char == FIVE_LETTER_WORDS[gw.get_current_row()][i]:
                    gw.set_square_color(gw.get_current_row(), i, WordleGWindow.CORRECT_COLOR)
                elif char in FIVE_LETTER_WORDS[gw.get_current_row()]:
                    gw.set_square_color(gw.get_current_row(), i, WordleGWindow.PRESENT_COLOR)
                else:
                    gw.set_square_color(gw.get_current_row(), i, WordleGWindow.MISSING_COLOR)
            
            # Increment current row
            gw.set_current_row(gw.get_current_row() + 1)
        else:
            gw.show_message("Not in word list")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

if __name__ == "__main__":
    wordle()