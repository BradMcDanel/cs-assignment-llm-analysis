import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    secret_word = random.choice(FIVE_LETTER_WORDS)

    def enter_action(s):
        guess = s.lower()
        if guess not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return

        current_row = gw.get_current_row()
        secret_word_chars = list(secret_word)
        guess_chars = list(guess)

        # First pass: Check for correct positions
        for col in range(N_COLS):
            if guess_chars[col] == secret_word_chars[col]:
                gw.set_square_color(current_row, col, CORRECT_COLOR)
                gw.set_key_color(guess_chars[col].upper(), CORRECT_COLOR)
                secret_word_chars[col] = None  # Mark as used
                guess_chars[col] = None  # Mark as processed

        # Second pass: Check for correct letters in wrong positions
        for col in range(N_COLS):
            if guess_chars[col] and guess_chars[col] in secret_word_chars:
                gw.set_square_color(current_row, col, PRESENT_COLOR)
                if gw.get_key_color(guess_chars[col].upper()) != CORRECT_COLOR:
                    gw.set_key_color(guess_chars[col].upper(), PRESENT_COLOR)
                secret_word_chars[secret_word_chars.index(guess_chars[col])] = None
            elif guess_chars[col]:
                if gw.get_key_color(guess_chars[col].upper()) not in [CORRECT_COLOR, PRESENT_COLOR]:
                    gw.set_key_color(guess_chars[col].upper(), MISSING_COLOR)
                gw.set_square_color(current_row, col, MISSING_COLOR)

        # Move to the next row if the guess is incorrect
        if guess != secret_word:
            if current_row < N_ROWS - 1:
                gw.set_current_row(current_row + 1)
            else:
                gw.show_message(f"The word was: {secret_word.upper()}")
        else:
            gw.show_message("Congratulations! You've guessed the word!")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()