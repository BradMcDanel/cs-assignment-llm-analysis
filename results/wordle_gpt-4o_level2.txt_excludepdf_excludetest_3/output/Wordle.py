import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    def enter_action(s):
        current_row = gw.get_current_row()
        entered_word = ''.join([gw.get_square_letter(current_row, col) for col in range(N_COLS)])
        
        if entered_word.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
        else:
            # Check each letter and color accordingly
            secret_word_copy = list(secret_word)
            for col in range(N_COLS):
                letter = entered_word[col]
                if letter == secret_word[col]:
                    gw.set_square_color(current_row, col, CORRECT_COLOR)
                    gw.set_key_color(letter, CORRECT_COLOR)
                    secret_word_copy[col] = None  # Mark this letter as used
                elif letter in secret_word_copy:
                    gw.set_square_color(current_row, col, PRESENT_COLOR)
                    if gw.get_key_color(letter) != CORRECT_COLOR:
                        gw.set_key_color(letter, PRESENT_COLOR)
                    secret_word_copy[secret_word_copy.index(letter)] = None  # Mark this letter as used
                else:
                    gw.set_square_color(current_row, col, MISSING_COLOR)
                    if gw.get_key_color(letter) not in (CORRECT_COLOR, PRESENT_COLOR):
                        gw.set_key_color(letter, MISSING_COLOR)
                    
            if entered_word == secret_word:
                gw.show_message("Congratulations!")
            else:
                gw.set_current_row(current_row + 1)

    # Create the graphics window
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    # Pick a random word from the list
    secret_word = random.choice(FIVE_LETTER_WORDS).upper()

# Startup code
if __name__ == "__main__":
    wordle()