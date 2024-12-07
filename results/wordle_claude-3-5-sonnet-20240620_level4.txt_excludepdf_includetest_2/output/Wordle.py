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
        for col in range(N_COLS):
            letter = gw.get_square_letter(current_row, col)
            if letter == hidden_word[col]:
                gw.set_square_color(current_row, col, CORRECT_COLOR)
                gw.set_key_color(letter, CORRECT_COLOR)
                correct_count += 1
            elif letter in hidden_word:
                gw.set_square_color(current_row, col, PRESENT_COLOR)
                if gw.get_key_color(letter) != CORRECT_COLOR:
                    gw.set_key_color(letter, PRESENT_COLOR)
            else:
                gw.set_square_color(current_row, col, MISSING_COLOR)
                gw.set_key_color(letter, MISSING_COLOR)

        # Check if the word is correct
        if correct_count == N_COLS:
            gw.show_message("Congratulations! You've won!")
        elif current_row == N_ROWS - 1:
            gw.show_message(f"Game over. The word was {hidden_word}")
        else:
            current_row += 1
            gw.set_current_row(current_row)

    # Choose a random word
    hidden_word = random.choice(FIVE_LETTER_WORDS).upper()
    
    # Initialize the game window
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    # Set up the game
    current_row = 0
    gw.set_current_row(current_row)

# Startup code
if __name__ == "__main__":
    wordle()