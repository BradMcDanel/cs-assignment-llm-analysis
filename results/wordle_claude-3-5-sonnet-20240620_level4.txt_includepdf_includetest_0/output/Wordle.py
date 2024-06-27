import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    # Choose a random word from the dictionary
    secret_word = random.choice(FIVE_LETTER_WORDS).upper()
    
    # Create the game window
    gw = WordleGWindow()

    def enter_action(s):
        nonlocal secret_word
        
        # Check if the guess is a valid word
        if s.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return

        # Get the current row
        current_row = gw.get_current_row()

        # Check each letter and update colors
        for col in range(N_COLS):
            letter = s[col]
            if letter == secret_word[col]:
                color = CORRECT_COLOR
            elif letter in secret_word:
                color = PRESENT_COLOR
            else:
                color = MISSING_COLOR
            
            gw.set_square_color(current_row, col, color)
            
            # Update key color
            current_key_color = gw.get_key_color(letter)
            if current_key_color != CORRECT_COLOR:
                gw.set_key_color(letter, color)

        # Check if the word is correct
        if s == secret_word:
            gw.show_message("Congratulations!")
        elif current_row == N_ROWS - 1:
            gw.show_message(f"Game over. The word was {secret_word}")
        else:
            gw.set_current_row(current_row + 1)

    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()