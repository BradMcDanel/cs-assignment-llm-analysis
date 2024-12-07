import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS
from WordleGraphics import CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    # Choose a random word from the dictionary
    target_word = random.choice(FIVE_LETTER_WORDS).upper()
    
    # Create the game window
    gw = WordleGWindow()
    
    def enter_action(s):
        # Get the current row
        row = gw.get_current_row()
        
        # Check if the guess is a valid word
        if s.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return
        
        # Check the guess against the target word
        for col in range(N_COLS):
            letter = s[col]
            if letter == target_word[col]:
                color = CORRECT_COLOR
            elif letter in target_word:
                color = PRESENT_COLOR
            else:
                color = MISSING_COLOR
            gw.set_square_color(row, col, color)
            gw.set_key_color(letter, color)
        
        # Check if the guess is correct
        if s == target_word:
            gw.show_message("Congratulations!")
        elif row == N_ROWS - 1:
            gw.show_message(f"The word was {target_word}")
        else:
            gw.set_current_row(row + 1)

    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()