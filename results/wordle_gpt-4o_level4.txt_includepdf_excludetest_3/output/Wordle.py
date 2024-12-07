import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    # Randomly choose a word from the dictionary
    secret_word = random.choice(FIVE_LETTER_WORDS)
    
    # Set up the game window
    gw = WordleGWindow()

    def enter_action(guess):
        current_row = gw.get_current_row()
        
        # Check if the guess is valid
        if guess.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return
        
        # Color the squares based on the guess
        letter_count = {}
        for letter in secret_word:
            letter_count[letter] = letter_count.get(letter, 0) + 1

        # First pass to color correct letters
        for i in range(N_COLS):
            if guess[i].lower() == secret_word[i]:
                gw.set_square_color(current_row, i, CORRECT_COLOR)
                letter_count[guess[i].lower()] -= 1
            else:
                gw.set_square_color(current_row, i, MISSING_COLOR)
        
        # Second pass to color present letters
        for i in range(N_COLS):
            if gw.get_square_color(current_row, i) == MISSING_COLOR:
                if letter_count.get(guess[i].lower(), 0) > 0:
                    gw.set_square_color(current_row, i, PRESENT_COLOR)
                    letter_count[guess[i].lower()] -= 1

        # Check if the guess is correct
        if guess.lower() == secret_word:
            gw.show_message("Congratulations! You've guessed the word.")
        else:
            if current_row < N_ROWS - 1:
                gw.set_current_row(current_row + 1)
            else:
                gw.show_message(f"Sorry! The word was {secret_word}")

    # Add the enter action listener
    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()