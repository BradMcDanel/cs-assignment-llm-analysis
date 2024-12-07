from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, KEY_COLOR

def wordle():

    def enter_action(s):
        gw.show_message("You have to implement this method.")
        if s.lower() in FIVE_LETTER_WORDS:
            for col in range(N_COLS):
                if s[col] == FIVE_LETTER_WORDS[0][col]:
                    gw.set_square_color(0, col, CORRECT_COLOR)
                elif s[col] in FIVE_LETTER_WORDS[0]:
                    gw.set_square_color(0, col, PRESENT_COLOR)
                else:
                    gw.set_square_color(0, col, MISSING_COLOR)
            for key in s:
                gw.set_key_color(key.upper(), KEY_COLOR)

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code

if __name__ == "__main__":
    wordle()