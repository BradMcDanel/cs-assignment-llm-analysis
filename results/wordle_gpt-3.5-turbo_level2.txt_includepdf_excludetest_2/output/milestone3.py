# Milestone #3: Color the boxes

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    def enter_action(s):
        if s.lower() in FIVE_LETTER_WORDS:
            for i in range(N_COLS):
                if s[i] == word[i]:
                    gw.set_square_color(gw.get_current_row(), i, CORRECT_COLOR)
                elif s[i] in word:
                    gw.set_square_color(gw.get_current_row(), i, PRESENT_COLOR)
                else:
                    gw.set_square_color(gw.get_current_row(), i, MISSING_COLOR)
            gw.set_current_row(gw.get_current_row() + 1)
        else:
            gw.show_message("Not in word list")

    gw = WordleGWindow()
    word = random.choice(FIVE_LETTER_WORDS)
    gw.add_enter_listener(enter_action)

if __name__ == "__main__":
    wordle()