# Milestone #3: Color the boxes

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def milestone3():
    def enter_action(s):
        if s.lower() in FIVE_LETTER_WORDS:
            for col, letter in enumerate(s):
                if letter in FIVE_LETTER_WORDS:
                    if letter == FIVE_LETTER_WORDS[col]:
                        gw.set_square_color(gw.get_current_row(), col, CORRECT_COLOR)
                    else:
                        gw.set_square_color(gw.get_current_row(), col, PRESENT_COLOR)
                else:
                    gw.set_square_color(gw.get_current_row(), col, MISSING_COLOR)
            gw.set_current_row(gw.get_current_row() + 1)
        else:
            gw.show_message("Not in word list")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    milestone3()