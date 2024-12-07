import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    # Choose a random word from the dictionary
    target_word = random.choice(FIVE_LETTER_WORDS).upper()
    
    # Initialize the game window
    gw = WordleGWindow()
    
    def enter_action(s):
        nonlocal target_word
        
        # Check if the guess is a valid word
        if s.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return
        
        # Get the current row
        current_row = gw.get_current_row()
        
        # Check each letter of the guess
        for col in range(N_COLS):
            letter = s[col]
            if letter == target_word[col]:
                color = CORRECT_COLOR
            elif letter in target_word:
                color = PRESENT_COLOR
            else:
                color = MISSING_COLOR
            
            # Set the color of the square and the key
            gw.set_square_color(current_row, col, color)
            gw.set_key_color(letter, color)
        
        # Check if the guess is correct
        if s == target_word:
            gw.show_message("Congratulations!")
        else:
            # Move to the next row
            next_row = current_row + 1
            if next_row < N_ROWS:
                gw.set_current_row(next_row)
            else:
                gw.show_message(f"Game over. The word was {target_word}")

    # Add the enter listener
    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()