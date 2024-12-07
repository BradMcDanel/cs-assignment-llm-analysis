"""
This module implements the Wordle game logic.
"""

import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    # Pick a random word from the dictionary
    target_word = random.choice(FIVE_LETTER_WORDS).upper()
    gw = WordleGWindow()

    def enter_action(guess):
        guess = guess.strip().upper()

        # Milestone #2: Check if the guess is a valid word
        if guess.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return

        # Milestone #3: Color the boxes
        current_row = gw.get_current_row()
        target_letter_count = {ch: target_word.count(ch) for ch in target_word}
        
        # First pass: Check for correct positions
        for col in range(N_COLS):
            letter = guess[col]
            if letter == target_word[col]:
                gw.set_square_color(current_row, col, CORRECT_COLOR)
                target_letter_count[letter] -= 1
            else:
                gw.set_square_color(current_row, col, MISSING_COLOR)

        # Second pass: Check for present but misplaced letters
        for col in range(N_COLS):
            letter = guess[col]
            if gw.get_square_color(current_row, col) != CORRECT_COLOR:  # Already correctly placed ones are skipped
                if letter in target_letter_count and target_letter_count[letter] > 0:
                    gw.set_square_color(current_row, col, PRESENT_COLOR)
                    target_letter_count[letter] -= 1

        # Milestone #4: Color the keys
        for col in range(N_COLS):
            letter = guess[col]
            if gw.get_square_color(current_row, col) == CORRECT_COLOR:
                gw.set_key_color(letter, CORRECT_COLOR)
            elif gw.get_square_color(current_row, col) == PRESENT_COLOR and gw.get_key_color(letter) != CORRECT_COLOR:
                gw.set_key_color(letter, PRESENT_COLOR)
            elif gw.get_key_color(letter) not in (CORRECT_COLOR, PRESENT_COLOR):
                gw.set_key_color(letter, MISSING_COLOR)

        # Check for win or progress to the next row
        if guess == target_word:
            gw.show_message("Congratulations! You guessed the word!")
        else:
            if current_row < N_ROWS - 1:
                gw.set_current_row(current_row + 1)
            else:
                gw.show_message(f"Game over! The word was {target_word}")

    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()