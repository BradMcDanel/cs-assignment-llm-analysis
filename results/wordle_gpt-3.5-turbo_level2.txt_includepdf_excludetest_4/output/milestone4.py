# Milestone #4: Color the keys

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, KEY_COLOR

def milestone4():
    def enter_action(s):
        if s in FIVE_LETTER_WORDS:
            for i in range(N_COLS):
                if s[i] == gw.get_square_letter(0, i):
                    gw.set_square_color(0, i, CORRECT_COLOR)
                elif s[i] in gw.get_square_letter(0):
                    gw.set_square_color(0, i, PRESENT_COLOR)
                else:
                    gw.set_square_color(0, i, MISSING_COLOR)
            for ch in s:
                gw.set_key_color(ch, KEY_COLOR)
        else:
            gw.show_message("Not in word list")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

if __name__ == "__main__":
    milestone4()