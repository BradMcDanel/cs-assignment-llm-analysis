"""
This module is the implementation file for the Wordle assignment.
"""

import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    """
    Main function to run the Wordle game.
    """
    
    # Select a random word from the word list
    secret_word = random.choice(FIVE_LETTER_WORDS).upper()

    def enter_action(guess):
        """
        This function is triggered when the ENTER key is pressed.
        It processes the user's word guess and updates the UI.
        """
        current_row = gw.get_current_row()

        # Check if the word is in the dictionary
        if guess.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return

        # Check each letter in the guess
        for i in range(N_COLS):
            letter = guess[i]
            if letter == secret_word[i]:
                gw.set_square_color(current_row, i, CORRECT_COLOR)
            elif letter in secret_word:
                gw.set_square_color(current_row, i, PRESENT_COLOR)
            else:
                gw.set_square_color(current_row, i, MISSING_COLOR)
            gw.set_square_letter(current_row, i, letter)
        
        # Update the color of the keyboard keys
        for letter in set(guess):
            if letter in secret_word:
                if guess.count(letter) <= secret_word.count(letter):
                    gw.set_key_color(letter, PRESENT_COLOR)
                else:
                    gw.set_key_color(letter, MISSING_COLOR)
            else:
                gw.set_key_color(letter, MISSING_COLOR)

        # Check if the guess is correct
        if guess == secret_word:
            gw.show_message("Congratulations! You've guessed the word!")
        elif current_row == N_ROWS - 1:
            gw.show_message(f"Game over! The word was {secret_word}.")
        else:
            gw.set_current_row(current_row + 1)

    # Initialize the graphics window
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()