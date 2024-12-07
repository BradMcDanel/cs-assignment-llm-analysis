import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    def enter_action(s):
        current_row = gw.get_current_row()
        if s.lower() in FIVE_LETTER_WORDS:
            # Check if the guess is correct
            if s.upper() == secret_word:
                gw.show_message("Congratulations!")
                for col in range(N_COLS):
                    gw.set_square_color(current_row, col, CORRECT_COLOR)
            else:
                # Color the boxes and keys
                used_indices = []
                # First pass for correct letters
                for col in range(N_COLS):
                    if s[col] == secret_word[col]:
                        gw.set_square_color(current_row, col, CORRECT_COLOR)
                        gw.set_key_color(s[col], CORRECT_COLOR)
                        used_indices.append(col)
                # Second pass for present letters
                for col in range(N_COLS):
                    if col not in used_indices:
                        if s[col] in secret_word:
                            if secret_word.index(s[col]) not in used_indices:
                                gw.set_square_color(current_row, col, PRESENT_COLOR)
                                gw.set_key_color(s[col], PRESENT_COLOR)
                                used_indices.append(secret_word.index(s[col]))
                        else:
                            gw.set_square_color(current_row, col, MISSING_COLOR)
                            gw.set_key_color(s[col], MISSING_COLOR)
            gw.set_current_row(current_row + 1)
        else:
            gw.show_message("Not in word list")

    # Create the graphics window
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    # Pick a random word from the list
    secret_word = random.choice(FIVE_LETTER_WORDS).upper()

# Startup code
if __name__ == "__main__":
    wordle()