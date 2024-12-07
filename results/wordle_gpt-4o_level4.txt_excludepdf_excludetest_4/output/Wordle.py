import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, N_ROWS, N_COLS

def wordle():
    # Select a random word from the dictionary
    secret_word = random.choice(FIVE_LETTER_WORDS).upper()

    def enter_action(guess):
        guess = guess.upper()
        current_row = gw.get_current_row()

        # Check if the guess is a valid word
        if guess.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return

        # Color the boxes based on the guess
        secret_word_count = {}
        for letter in secret_word:
            secret_word_count[letter] = secret_word_count.get(letter, 0) + 1

        # First pass: Check for correct letters in the correct position
        for col in range(N_COLS):
            gw.set_square_letter(current_row, col, guess[col])
            if guess[col] == secret_word[col]:
                gw.set_square_color(current_row, col, CORRECT_COLOR)
                secret_word_count[guess[col]] -= 1

        # Second pass: Check for correct letters in the wrong position
        for col in range(N_COLS):
            if gw.get_square_color(current_row, col) != CORRECT_COLOR:
                if guess[col] in secret_word and secret_word_count[guess[col]] > 0:
                    gw.set_square_color(current_row, col, PRESENT_COLOR)
                    secret_word_count[guess[col]] -= 1
                else:
                    gw.set_square_color(current_row, col, MISSING_COLOR)

        # Update key colors
        for letter in guess:
            if letter in secret_word:
                if secret_word.count(letter) > 0:
                    gw.set_key_color(letter, CORRECT_COLOR if guess[secret_word.index(letter)] == letter else PRESENT_COLOR)
                else:
                    gw.set_key_color(letter, MISSING_COLOR)
            else:
                gw.set_key_color(letter, MISSING_COLOR)

        # Check if the guess is correct
        if guess == secret_word:
            gw.show_message("Congratulations! You've guessed the word!")
        elif current_row == N_ROWS - 1:
            gw.show_message(f"Game over! The word was {secret_word}")

        # Move to the next row
        gw.set_current_row(current_row + 1)

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()