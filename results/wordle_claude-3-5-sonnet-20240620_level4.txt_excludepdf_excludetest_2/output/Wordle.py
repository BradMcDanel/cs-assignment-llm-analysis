import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, N_ROWS, N_COLS

def wordle():
    # Choose a random word from the dictionary
    secret_word = random.choice(FIVE_LETTER_WORDS).upper()
    
    def enter_action(s):
        current_row = gw.get_current_row()
        
        # Check if the entered word is in the word list
        if s.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return
        
        # Color the boxes
        color_guess(s, current_row)
        
        # Check if the guess is correct
        if s == secret_word:
            gw.show_message("Congratulations!")
        elif current_row == N_ROWS - 1:
            gw.show_message(f"The word was {secret_word}")
        else:
            gw.set_current_row(current_row + 1)

    def color_guess(guess, row):
        # Create a list to keep track of used letters in the secret word
        secret_letters = list(secret_word)
        
        # First pass: Mark correct letters
        for i in range(N_COLS):
            if guess[i] == secret_word[i]:
                gw.set_square_color(row, i, CORRECT_COLOR)
                gw.set_key_color(guess[i], CORRECT_COLOR)
                secret_letters[i] = None
        
        # Second pass: Mark present and missing letters
        for i in range(N_COLS):
            if gw.get_square_color(row, i) != CORRECT_COLOR:
                if guess[i] in secret_letters:
                    gw.set_square_color(row, i, PRESENT_COLOR)
                    if gw.get_key_color(guess[i]) != CORRECT_COLOR:
                        gw.set_key_color(guess[i], PRESENT_COLOR)
                    secret_letters[secret_letters.index(guess[i])] = None
                else:
                    gw.set_square_color(row, i, MISSING_COLOR)
                    if gw.get_key_color(guess[i]) == "":
                        gw.set_key_color(guess[i], MISSING_COLOR)

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()