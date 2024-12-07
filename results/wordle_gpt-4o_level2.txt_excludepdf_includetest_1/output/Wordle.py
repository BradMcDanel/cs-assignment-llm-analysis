import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    # Pick a random word for the game
    secret_word = random.choice(FIVE_LETTER_WORDS)
    current_row = 0

    def enter_action(s):
        nonlocal current_row
        guess = s.strip().lower()

        if len(guess) != N_COLS or guess not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return

        gw.show_message("")  # Clear any previous messages

        # Check for correct, present, and missing letters
        secret_word_chars = list(secret_word)
        guess_chars = list(guess)
        colors = [MISSING_COLOR] * N_COLS

        # First pass for correct positions
        for i in range(N_COLS):
            if guess_chars[i] == secret_word_chars[i]:
                colors[i] = CORRECT_COLOR
                secret_word_chars[i] = None  # Mark as used

        # Second pass for present letters
        for i in range(N_COLS):
            if colors[i] == CORRECT_COLOR:
                continue
            if guess_chars[i] in secret_word_chars:
                colors[i] = PRESENT_COLOR
                secret_word_chars[secret_word_chars.index(guess_chars[i])] = None  # Mark as used

        # Set colors and letters in the grid
        for i in range(N_COLS):
            gw.set_square_letter(current_row, i, guess[i].upper())
            gw.set_square_color(current_row, i, colors[i])
            gw.set_key_color(guess[i].upper(), colors[i])

        if guess == secret_word:
            gw.show_message("Congratulations! You've guessed the word!")
        elif current_row == N_ROWS - 1:
            gw.show_message(f"Game over! The word was: {secret_word.upper()}")
        else:
            current_row += 1
            gw.set_current_row(current_row)

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()