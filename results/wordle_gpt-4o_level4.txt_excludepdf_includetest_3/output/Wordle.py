import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, N_ROWS, N_COLS

def wordle():
    def enter_action(s):
        # Check if the entered word is valid
        current_row = gw.get_current_row()
        entered_word = ''.join(gw.get_square_letter(current_row, col) for col in range(N_COLS)).lower()

        if entered_word not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return

        # Color the boxes based on the entered word and the secret word
        for col in range(N_COLS):
            letter = gw.get_square_letter(current_row, col)
            if letter == secret_word[col]:
                gw.set_square_color(current_row, col, CORRECT_COLOR)
            elif letter in secret_word:
                gw.set_square_color(current_row, col, PRESENT_COLOR)
            else:
                gw.set_square_color(current_row, col, MISSING_COLOR)

        # Check for win condition
        if entered_word == secret_word:
            gw.show_message("Congratulations! You've guessed the word.")
        else:
            # Move to the next row
            gw.set_current_row(current_row + 1)

    # Select a random word from the list
    secret_word = random.choice(FIVE_LETTER_WORDS).upper()

    # Create the graphics window and set up the game
    gw = WordleGWindow()
    # Set random word in the first row for Milestone #1
    for col, letter in enumerate(secret_word):
        gw.set_square_letter(0, col, letter)
    
    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()