import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    def enter_action(s):
        guess = s.upper()
        
        if guess.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return
        
        row = gw.get_current_row()
        
        # Check and color the guess
        for col in range(N_COLS):
            letter = guess[col]
            if letter == word[col]:
                color = CORRECT_COLOR
            elif letter in word:
                color = PRESENT_COLOR
            else:
                color = MISSING_COLOR
            
            gw.set_square_color(row, col, color)
            
            # Update key color
            current_key_color = gw.get_key_color(letter)
            if current_key_color != CORRECT_COLOR:
                gw.set_key_color(letter, color)
        
        if guess == word:
            gw.show_message("Congratulations!")
        elif row == N_ROWS - 1:
            gw.show_message(f"The word was {word}")
        else:
            gw.set_current_row(row + 1)

    # Choose a random word
    word = random.choice(FIVE_LETTER_WORDS).upper()
    
    # Create window and set up enter action
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Constants
N_ROWS = 6
N_COLS = 5

# Startup code
if __name__ == "__main__":
    wordle()