import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, N_ROWS, N_COLS

def wordle():
    # Select a random word from FIVE_LETTER_WORDS
    secret_word = random.choice(FIVE_LETTER_WORDS)

    # Create WordleGWindow instance
    gw = WordleGWindow()

    # Function to handle the enter action
    def enter_action(guess):
        # Get the current row
        current_row = gw.get_current_row()
        
        # Validate the guess
        if guess.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return
        
        # Check if the guess is correct
        if guess.lower() == secret_word:
            gw.show_message("Congratulations! You've guessed the word!")
            color_keys_and_squares(current_row, guess, secret_word)
            return
        
        # Color the squares based on the guess
        color_keys_and_squares(current_row, guess, secret_word)
        
        # Move to the next row
        if current_row < N_ROWS - 1:
            gw.set_current_row(current_row + 1)
        else:
            gw.show_message(f"You've used all your guesses! The word was {secret_word.upper()}.")

    # Function to color the squares and keys
    def color_keys_and_squares(row, guess, secret_word):
        # To handle the coloring of keys
        key_colors = {}

        # Create a mutable copy of the secret word to mark off letters as they are used
        remaining_letters = list(secret_word)

        # First pass: Check for correct letter and position
        for col in range(N_COLS):
            guess_letter = guess[col].lower()
            if guess_letter == secret_word[col]:
                gw.set_square_color(row, col, CORRECT_COLOR)
                key_colors[guess_letter] = CORRECT_COLOR
                remaining_letters[col] = None  # Mark as used

        # Second pass: Check for correct letter but wrong position
        for col in range(N_COLS):
            guess_letter = guess[col].lower()
            if gw.get_square_color(row, col) != CORRECT_COLOR:  # If not already colored correctly
                if guess_letter in remaining_letters:
                    gw.set_square_color(row, col, PRESENT_COLOR)
                    key_colors.setdefault(guess_letter, PRESENT_COLOR)
                    remaining_letters[remaining_letters.index(guess_letter)] = None  # Mark as used
                else:
                    gw.set_square_color(row, col, MISSING_COLOR)
                    key_colors.setdefault(guess_letter, MISSING_COLOR)

        # Update key colors
        for letter, color in key_colors.items():
            gw.set_key_color(letter.upper(), color)

    # Add the enter listener
    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()