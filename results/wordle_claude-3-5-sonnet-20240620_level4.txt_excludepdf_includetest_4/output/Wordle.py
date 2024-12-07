import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, N_ROWS, N_COLS

def wordle():
    # Choose a random word from the dictionary
    secret_word = random.choice(FIVE_LETTER_WORDS).upper()
    
    gw = WordleGWindow()
    current_row = 0

    def enter_action(s):
        nonlocal current_row
        
        # Check if the entered word is in the dictionary
        if s.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return

        # Color the boxes
        color_boxes(s, secret_word, current_row)

        # Color the keys
        color_keys(s, secret_word)

        # Check if the word is correct
        if s == secret_word:
            gw.show_message("Congratulations!")
        elif current_row == N_ROWS - 1:
            gw.show_message(f"The word was {secret_word}")
        else:
            current_row += 1
            gw.set_current_row(current_row)

    def color_boxes(guess, secret, row):
        # First pass: mark correct letters
        for col in range(N_COLS):
            if guess[col] == secret[col]:
                gw.set_square_color(row, col, CORRECT_COLOR)
                secret = secret[:col] + ' ' + secret[col+1:]  # Mark as used

        # Second pass: mark present and missing letters
        for col in range(N_COLS):
            if gw.get_square_color(row, col) != CORRECT_COLOR:
                if guess[col] in secret:
                    gw.set_square_color(row, col, PRESENT_COLOR)
                    idx = secret.index(guess[col])
                    secret = secret[:idx] + ' ' + secret[idx+1:]  # Mark as used
                else:
                    gw.set_square_color(row, col, MISSING_COLOR)

    def color_keys(guess, secret):
        for letter in guess:
            current_color = gw.get_key_color(letter)
            if letter == secret[guess.index(letter)]:
                new_color = CORRECT_COLOR
            elif letter in secret:
                new_color = PRESENT_COLOR
            else:
                new_color = MISSING_COLOR

            if current_color != CORRECT_COLOR:
                if current_color != PRESENT_COLOR or new_color == CORRECT_COLOR:
                    gw.set_key_color(letter, new_color)

    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()