# Milestone #4: Color the keys on the virtual keyboard
from WordleGraphics import WordleGWindow, KEY_COLOR

def milestone4():
    def enter_action(s):
        if s.lower() in FIVE_LETTER_WORDS:
            for i in range(N_COLS):
                if s[i].lower() == FIVE_LETTER_WORDS[FIVE_LETTER_WORDS.index(s.lower())][i]:
                    gw.set_square_color(gw.get_current_row(), i, CORRECT_COLOR)
                elif s[i].lower() in FIVE_LETTER_WORDS[FIVE_LETTER_WORDS.index(s.lower())]:
                    gw.set_square_color(gw.get_current_row(), i, PRESENT_COLOR)
                else:
                    gw.set_square_color(gw.get_current_row(), i, MISSING_COLOR)
            for letter in s:
                gw.set_key_color(letter.upper(), KEY_COLOR)
            gw.set_current_row(gw.get_current_row() + 1)
        else:
            gw.show_message("Not in word list")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

if __name__ == "__main__":
    milestone4()