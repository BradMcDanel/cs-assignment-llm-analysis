import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    # Choose a random word from the dictionary
    secret_word = random.choice(FIVE_LETTER_WORDS).upper()
    
    def enter_action(guess):
        nonlocal secret_word
        guess = guess.lower()
        
        if guess not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return
        
        # Convert guess to uppercase for display
        guess = guess.upper()
        
        # Check if the guess is correct
        if guess == secret_word:
            color_guess(guess)
            gw.show_message("Congratulations!")
            return
        
        color_guess(guess)
        
        # Move to the next row
        current_row = gw.get_current_row()
        if current_row < N_ROWS - 1:
            gw.set_current_row(current_row + 1)
        else:
            gw.show_message(f"Game over! The word was {secret_word}")

    def color_guess(guess):
        row = gw.get_current_row()
        remaining_letters = list(secret_word)
        
        # First pass: mark correct letters
        for col in range(N_COLS):
            if guess[col] == secret_word[col]:
                gw.set_square_color(row, col, CORRECT_COLOR)
                gw.set_key_color(guess[col], CORRECT_COLOR)
                remaining_letters[col] = None
            else:
                gw.set_square_color(row, col, MISSING_COLOR)
        
        # Second pass: mark present letters
        for col in range(N_COLS):
            if guess[col] != secret_word[col]:
                if guess[col] in remaining_letters:
                    gw.set_square_color(row, col, PRESENT_COLOR)
                    if gw.get_key_color(guess[col]) != CORRECT_COLOR:
                        gw.set_key_color(guess[col], PRESENT_COLOR)
                    remaining_letters[remaining_letters.index(guess[col])] = None
                else:
                    if gw.get_key_color(guess[col]) == MISSING_COLOR:
                        gw.set_key_color(guess[col], MISSING_COLOR)

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()