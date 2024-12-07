# Milestone #4: Color the keys

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, KEY_COLOR

def milestone4():
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

    def color_keys():
        used_letters = set()
        for row in range(gw.get_current_row()):
            for col in range(N_COLS):
                letter = gw.get_square_letter(row, col)
                if letter != " ":
                    used_letters.add(letter)

        for key in gw._keys.keys():
            if key in used_letters:
                gw.set_key_color(key, KEY_COLOR)

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
    gw.add_enter_listener(color_keys)

# Startup code
if __name__ == "__main__":
    milestone4()