import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    def enter_action(s):
        user_word = s.lower()
        if user_word in FIVE_LETTER_WORDS:
            for col in range(N_COLS):
                letter = user_word[col]
                if letter == chosen_word[col]:
                    gw.set_square_color(gw.get_current_row(), col, CORRECT_COLOR)
                    gw.set_key_color(letter.upper(), CORRECT_COLOR)
                elif letter in chosen_word:
                    if gw.get_key_color(letter.upper()) != CORRECT_COLOR:
                        gw.set_square_color(gw.get_current_row(), col, PRESENT_COLOR)
                        gw.set_key_color(letter.upper(), PRESENT_COLOR)
                else:
                    gw.set_square_color(gw.get_current_row(), col, MISSING_COLOR)
                    gw.set_key_color(letter.upper(), MISSING_COLOR)
            gw.show_message("Processed your guess.")
            if user_word == chosen_word:
                gw.show_message("Congratulations! You guessed the word.")
            gw.set_current_row(gw.get_current_row() + 1)
        else:
            gw.show_message("Not in word list")

    gw = WordleGWindow()
    chosen_word = random.choice(FIVE_LETTER_WORDS)
    gw.add_enter_listener(enter_action)

if __name__ == "__main__":
    wordle()