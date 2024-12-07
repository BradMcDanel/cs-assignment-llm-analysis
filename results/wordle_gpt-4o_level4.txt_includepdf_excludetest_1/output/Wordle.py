import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    # Pick a random word from the dictionary
    secret_word = random.choice(FIVE_LETTER_WORDS)
    
    def enter_action(guess):
        # Convert guess and secret_word to lowercase for comparison
        guess = guess.lower()
        
        # Check if the guess is a valid word
        if guess not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list.")
            return
        
        # Get the current row to display the guess
        current_row = gw.get_current_row()
        
        # Check if the guess is correct
        if guess == secret_word:
            gw.show_message("Congratulations! You've guessed the word.")
            for col in range(N_COLS):
                gw.set_square_color(current_row, col, CORRECT_COLOR)
                gw.set_key_color(guess[col].upper(), CORRECT_COLOR)
            return
        
        # Color the squares based on the guess
        secret_word_count = {}
        for char in secret_word:
            secret_word_count[char] = secret_word_count.get(char, 0) + 1
        
        for col in range(N_COLS):
            guess_char = guess[col]
            secret_char = secret_word[col]
            
            if guess_char == secret_char:
                gw.set_square_color(current_row, col, CORRECT_COLOR)
                gw.set_key_color(guess_char.upper(), CORRECT_COLOR)
                secret_word_count[guess_char] -= 1
            else:
                gw.set_square_color(current_row, col, MISSING_COLOR)
        
        # Mark present letters
        for col in range(N_COLS):
            guess_char = guess[col]
            if gw.get_square_color(current_row, col) != CORRECT_COLOR and guess_char in secret_word_count and secret_word_count[guess_char] > 0:
                gw.set_square_color(current_row, col, PRESENT_COLOR)
                if gw.get_key_color(guess_char.upper()) != CORRECT_COLOR:
                    gw.set_key_color(guess_char.upper(), PRESENT_COLOR)
                secret_word_count[guess_char] -= 1
        
        # Move to the next row
        gw.set_current_row(current_row + 1)
        if current_row + 1 == N_ROWS:
            gw.show_message(f"The word was: {secret_word.upper()}. Better luck next time!")

    # Create the WordleGWindow and set up the enter listener
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()