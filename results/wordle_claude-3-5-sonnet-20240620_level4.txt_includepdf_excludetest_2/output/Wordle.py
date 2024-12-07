import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    # Choose a random word from the dictionary
    secret_word = random.choice(FIVE_LETTER_WORDS).upper()
    
    gw = WordleGWindow()
    
    def enter_action(s):
        s = s.upper()
        row = gw.get_current_row()
        
        # Check if the entered word is in the word list
        if s.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return
        
        # Color the boxes
        for col in range(N_COLS):
            letter = s[col]
            if letter == secret_word[col]:
                color = CORRECT_COLOR
            elif letter in secret_word:
                color = PRESENT_COLOR
            else:
                color = MISSING_COLOR
            gw.set_square_color(row, col, color)
            
            # Update key colors
            current_key_color = gw.get_key_color(letter)
            if current_key_color != CORRECT_COLOR:
                if color == CORRECT_COLOR or (color == PRESENT_COLOR and current_key_color != PRESENT_COLOR):
                    gw.set_key_color(letter, color)
                elif color == MISSING_COLOR and current_key_color == WordleGWindow.UNKNOWN_COLOR:
                    gw.set_key_color(letter, color)
        
        # Check if the word is correct
        if s == secret_word:
            gw.show_message("Congratulations!", "green")
        elif row == N_ROWS - 1:
            gw.show_message(f"The word was {secret_word}", "red")
        else:
            gw.set_current_row(row + 1)

    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()