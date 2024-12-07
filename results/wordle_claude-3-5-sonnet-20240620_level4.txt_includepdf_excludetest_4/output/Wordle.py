import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    # Choose a random word from the dictionary
    secret_word = random.choice(FIVE_LETTER_WORDS).upper()
    
    def enter_action(guess):
        nonlocal current_row
        guess = guess.lower()
        
        if guess not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return
        
        # Color the boxes
        for col in range(N_COLS):
            letter = guess[col].upper()
            if letter == secret_word[col]:
                color = CORRECT_COLOR
            elif letter in secret_word:
                color = PRESENT_COLOR
            else:
                color = MISSING_COLOR
            gw.set_square_color(current_row, col, color)
            
            # Update key colors
            current_key_color = gw.get_key_color(letter)
            if current_key_color != CORRECT_COLOR:
                if color == CORRECT_COLOR:
                    gw.set_key_color(letter, CORRECT_COLOR)
                elif color == PRESENT_COLOR and current_key_color != PRESENT_COLOR:
                    gw.set_key_color(letter, PRESENT_COLOR)
                elif current_key_color != PRESENT_COLOR:
                    gw.set_key_color(letter, MISSING_COLOR)
        
        # Check if the guess is correct
        if guess.upper() == secret_word:
            gw.show_message("Congratulations!")
        elif current_row == N_ROWS - 1:
            gw.show_message(f"The word was {secret_word}")
        else:
            current_row += 1
            gw.set_current_row(current_row)

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
    
    # Display the secret word in the first row (for debugging)
    for col, letter in enumerate(secret_word):
        gw.set_square_letter(0, col, letter)
    
    current_row = 0

# Startup code
if __name__ == "__main__":
    wordle()