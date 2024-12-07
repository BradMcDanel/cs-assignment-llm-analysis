import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    # Choose a random word from the dictionary
    secret_word = random.choice(FIVE_LETTER_WORDS).upper()
    
    # Create the game window
    gw = WordleGWindow()

    def enter_action(s):
        # Convert input to uppercase
        guess = s.upper()

        # Check if the guess is a valid word
        if guess.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return

        current_row = gw.get_current_row()

        # Check if the game is over
        if current_row >= N_ROWS:
            gw.show_message("Game over! The word was " + secret_word)
            return

        # Color the boxes and keys
        color_guess(guess, current_row)

        # Check if the guess is correct
        if guess == secret_word:
            gw.show_message("Congratulations!")
        else:
            # Move to the next row
            gw.set_current_row(current_row + 1)

    def color_guess(guess, row):
        # Create a list to keep track of which letters in the secret word have been matched
        secret_letters = list(secret_word)

        # First pass: mark correct letters
        for i in range(N_COLS):
            if guess[i] == secret_word[i]:
                gw.set_square_color(row, i, CORRECT_COLOR)
                gw.set_key_color(guess[i], CORRECT_COLOR)
                secret_letters[i] = None

        # Second pass: mark present and missing letters
        for i in range(N_COLS):
            if guess[i] == secret_word[i]:
                continue  # Already handled in the first pass
            elif guess[i] in secret_letters:
                gw.set_square_color(row, i, PRESENT_COLOR)
                if gw.get_key_color(guess[i]) != CORRECT_COLOR:
                    gw.set_key_color(guess[i], PRESENT_COLOR)
                secret_letters[secret_letters.index(guess[i])] = None
            else:
                gw.set_square_color(row, i, MISSING_COLOR)
                if gw.get_key_color(guess[i]) == CORRECT_COLOR:
                    gw.set_key_color(guess[i], CORRECT_COLOR)
                elif gw.get_key_color(guess[i]) == PRESENT_COLOR:
                    gw.set_key_color(guess[i], PRESENT_COLOR)
                else:
                    gw.set_key_color(guess[i], MISSING_COLOR)

    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()