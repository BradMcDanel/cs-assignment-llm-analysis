import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, N_ROWS, N_COLS

def wordle():
    # Step 1: Choose a random word
    secret_word = random.choice(FIVE_LETTER_WORDS).upper()
    
    # Initialize the game window
    gw = WordleGWindow()
    
    # Set up the enter action
    def enter_action(s):
        current_row = gw.get_current_row()
        
        # Check if the entered word is valid
        if s.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return
        
        # Color the boxes
        color_boxes(gw, current_row, s, secret_word)
        
        # Color the keys
        color_keys(gw, current_row)
        
        # Check if the word is correct
        if s == secret_word:
            gw.show_message("Congratulations!")
        elif current_row == N_ROWS - 1:
            gw.show_message(f"The word was {secret_word}")
        else:
            gw.set_current_row(current_row + 1)

    gw.add_enter_listener(enter_action)

def color_boxes(gw, row, guess, secret_word):
    used_positions = set()
    
    # First pass: mark correct letters
    for i in range(N_COLS):
        if guess[i] == secret_word[i]:
            gw.set_square_color(row, i, CORRECT_COLOR)
            used_positions.add(i)
    
    # Second pass: mark present and missing letters
    for i in range(N_COLS):
        if i not in used_positions:
            if guess[i] in secret_word and secret_word.count(guess[i]) > sum(1 for j in used_positions if secret_word[j] == guess[i]):
                gw.set_square_color(row, i, PRESENT_COLOR)
            else:
                gw.set_square_color(row, i, MISSING_COLOR)

def color_keys(gw, row):
    for col in range(N_COLS):
        letter = gw.get_square_letter(row, col)
        color = gw.get_square_color(row, col)
        current_key_color = gw.get_key_color(letter)
        
        if current_key_color != CORRECT_COLOR:
            if color == CORRECT_COLOR or (color == PRESENT_COLOR and current_key_color != PRESENT_COLOR):
                gw.set_key_color(letter, color)
            elif color == MISSING_COLOR and current_key_color is None:
                gw.set_key_color(letter, color)

# Startup code
if __name__ == "__main__":
    wordle()