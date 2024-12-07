import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow

CORRECT_COLOR = "#66BB66"
PRESENT_COLOR = "#CCBB66"
MISSING_COLOR = "#999999"

def wordle():
    def enter_action(s):
        if s.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
        else:
            check_guess(s)

    def check_guess(s):
        if s.lower() == FIVE_LETTER_WORDS[0]:  # Assume the first word in the list is the correct answer
            gw.show_message("Congratulations! You guessed the word.")
            return
        color_boxes(s)

    def color_boxes(s):
        for i in range(len(s)):
            if s[i] == FIVE_LETTER_WORDS[0][i]:
                gw.set_square_color(gw.get_current_row(), i, CORRECT_COLOR)
            elif s[i] in FIVE_LETTER_WORDS[0]:
                gw.set_square_color(gw.get_current_row(), i, PRESENT_COLOR)
            else:
                gw.set_square_color(gw.get_current_row(), i, MISSING_COLOR)

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

if __name__ == "__main__":
    wordle()