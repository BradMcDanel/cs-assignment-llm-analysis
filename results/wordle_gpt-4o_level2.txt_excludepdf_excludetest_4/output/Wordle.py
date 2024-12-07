"""
This module is the starter file for the Wordle assignment.
This implementation follows the milestones outlined in the assignment guide.
"""

import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, N_ROWS, N_COLS

def wordle():
    # Select a random word from the dictionary
    hidden_word = random.choice(FIVE_LETTER_WORDS).upper()
    
    def enter_action(guess):
        guess = guess.upper()
        
        # Check if the guess is a valid word
        if guess.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return
        
        # Get the current row
        row = gw.get_current_row()
        
        # Color the boxes based on the guess
        for col in range(N_COLS):
            letter = guess[col]
            if letter == hidden_word[col]:
                gw.set_square_color(row, col, CORRECT_COLOR)
                gw.set_key_color(letter, CORRECT_COLOR)
            elif letter in hidden_word:
                gw.set_square_color(row, col, PRESENT_COLOR)
                # Only update key if it's not already marked as CORRECT_COLOR
                if gw.get_key_color(letter) != CORRECT_COLOR:
                    gw.set_key_color(letter, PRESENT_COLOR)
            else:
                gw.set_square_color(row, col, MISSING_COLOR)
                gw.set_key_color(letter, MISSING_COLOR)
        
        # Check if the guess is correct
        if guess == hidden_word:
            gw.show_message("Congratulations! You've guessed the word!")
        elif row + 1 < N_ROWS:
            gw.set_current_row(row + 1)
        else:
            gw.show_message(f"Out of guesses! The word was {hidden_word}.")
    
    # Create the graphics window and add the enter listener
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()