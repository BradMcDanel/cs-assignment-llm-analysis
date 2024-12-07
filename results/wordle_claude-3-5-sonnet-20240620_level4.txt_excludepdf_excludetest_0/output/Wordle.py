import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, N_ROWS, N_COLS

def wordle():
    # Choose a random word
    hidden_word = random.choice(FIVE_LETTER_WORDS).upper()
    
    def enter_action(s):
        nonlocal hidden_word
        
        # Get the current row
        current_row = gw.get_current_row()
        
        # Check if the entered word is in the word list
        if s.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return
        
        # Color the boxes
        correct_count = 0
        used_positions = set()
        
        # First pass: Mark correct letters
        for i in range(N_COLS):
            if s[i] == hidden_word[i]:
                gw.set_square_color(current_row, i, CORRECT_COLOR)
                gw.set_key_color(s[i], CORRECT_COLOR)
                correct_count += 1
                used_positions.add(i)
        
        # Second pass: Mark present and missing letters
        for i in range(N_COLS):
            if i not in used_positions:
                if s[i] in hidden_word and s[i] != hidden_word[i]:
                    gw.set_square_color(current_row, i, PRESENT_COLOR)
                    if gw.get_key_color(s[i]) != CORRECT_COLOR:
                        gw.set_key_color(s[i], PRESENT_COLOR)
                else:
                    gw.set_square_color(current_row, i, MISSING_COLOR)
                    if gw.get_key_color(s[i]) == None:
                        gw.set_key_color(s[i], MISSING_COLOR)
        
        # Check if the word is correct
        if correct_count == N_COLS:
            gw.show_message("Congratulations! You've won!")
        else:
            # Move to the next row
            next_row = current_row + 1
            if next_row < N_ROWS:
                gw.set_current_row(next_row)
            else:
                gw.show_message(f"Game over. The word was {hidden_word}")

    # Create the graphics window
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()