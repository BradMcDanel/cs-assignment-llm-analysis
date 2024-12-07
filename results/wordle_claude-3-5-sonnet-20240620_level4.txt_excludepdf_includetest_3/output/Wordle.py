import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, N_ROWS, N_COLS

def wordle():
    def enter_action(s):
        nonlocal current_row
        
        # Check if the entered word is in the word list
        if s.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return

        # Color the boxes
        correct_count = 0
        word_copy = list(hidden_word)
        
        # First pass: Mark correct letters
        for col in range(N_COLS):
            if s[col] == hidden_word[col]:
                gw.set_square_color(current_row, col, CORRECT_COLOR)
                gw.set_key_color(s[col], CORRECT_COLOR)
                word_copy[col] = None
                correct_count += 1
            
        # Second pass: Mark present and missing letters
        for col in range(N_COLS):
            if s[col] == hidden_word[col]:
                continue
            elif s[col] in word_copy:
                gw.set_square_color(current_row, col, PRESENT_COLOR)
                if gw.get_key_color(s[col]) != CORRECT_COLOR:
                    gw.set_key_color(s[col], PRESENT_COLOR)
                word_copy[word_copy.index(s[col])] = None
            else:
                gw.set_square_color(current_row, col, MISSING_COLOR)
                if gw.get_key_color(s[col]) == None:
                    gw.set_key_color(s[col], MISSING_COLOR)

        # Check if the word is correct
        if correct_count == N_COLS:
            gw.show_message("Congratulations! You've won!")
        elif current_row == N_ROWS - 1:
            gw.show_message(f"Game over. The word was {hidden_word}")
        else:
            current_row += 1
            gw.set_current_row(current_row)

    # Initialize the game
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    # Choose a random word
    hidden_word = random.choice(FIVE_LETTER_WORDS).upper()
    current_row = 0

# Startup code
if __name__ == "__main__":
    wordle()