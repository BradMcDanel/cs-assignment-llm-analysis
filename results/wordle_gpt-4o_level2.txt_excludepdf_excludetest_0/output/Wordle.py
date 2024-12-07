import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    secret_word = random.choice(FIVE_LETTER_WORDS).upper()
    
    def enter_action(s):
        guess = s.upper()
        if guess.lower() in FIVE_LETTER_WORDS:
            gw.show_message("Guess is valid.")
            row = gw.get_current_row()
            
            # Create a temporary list to track used letters in the secret word
            secret_word_copy = list(secret_word)
            
            # First pass: Check for correct positions
            for i in range(N_COLS):
                if guess[i] == secret_word[i]:
                    gw.set_square_color(row, i, CORRECT_COLOR)
                    gw.set_key_color(guess[i], CORRECT_COLOR)
                    secret_word_copy[i] = None  # Mark as used
            
            # Second pass: Check for present but misplaced letters
            for i in range(N_COLS):
                if guess[i] != secret_word[i] and guess[i] in secret_word_copy:
                    gw.set_square_color(row, i, PRESENT_COLOR)
                    if gw.get_key_color(guess[i]) != CORRECT_COLOR:
                        gw.set_key_color(guess[i], PRESENT_COLOR)
                    secret_word_copy[secret_word_copy.index(guess[i])] = None  # Mark as used
                elif guess[i] != secret_word[i]:
                    gw.set_square_color(row, i, MISSING_COLOR)
                    if gw.get_key_color(guess[i]) not in [CORRECT_COLOR, PRESENT_COLOR]:
                        gw.set_key_color(guess[i], MISSING_COLOR)
            
            if guess == secret_word:
                gw.show_message("Congratulations! You found the word!")
            else:
                gw.set_current_row(row + 1)
        else:
            gw.show_message("Not in word list.")
    
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()