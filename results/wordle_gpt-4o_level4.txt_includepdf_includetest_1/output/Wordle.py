"""
This module completes the Wordle assignment.
"""

import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    # Select a random word from the dictionary
    target_word = random.choice(FIVE_LETTER_WORDS).upper()
    
    def enter_action(s):
        current_row = gw.get_current_row()
        
        # Check if entered word is of correct length and in the dictionary
        if len(s) != N_COLS or s.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return
        
        # Determine the coloring for each letter
        target_count = {}
        for letter in target_word:
            if letter in target_count:
                target_count[letter] += 1
            else:
                target_count[letter] = 1

        # First pass: Check for correct positions
        for i in range(N_COLS):
            if s[i] == target_word[i]:
                gw.set_square_color(current_row, i, CORRECT_COLOR)
                target_count[s[i]] -= 1
            else:
                gw.set_square_color(current_row, i, MISSING_COLOR)

        # Second pass: Check for present letters
        for i in range(N_COLS):
            if gw.get_square_color(current_row, i) != CORRECT_COLOR:
                if s[i] in target_count and target_count[s[i]] > 0:
                    gw.set_square_color(current_row, i, PRESENT_COLOR)
                    target_count[s[i]] -= 1

        # Update the keyboard colors
        for i in range(N_COLS):
            current_color = gw.get_key_color(s[i])
            if gw.get_square_color(current_row, i) == CORRECT_COLOR:
                gw.set_key_color(s[i], CORRECT_COLOR)
            elif gw.get_square_color(current_row, i) == PRESENT_COLOR and current_color != CORRECT_COLOR:
                gw.set_key_color(s[i], PRESENT_COLOR)
            elif gw.get_square_color(current_row, i) == MISSING_COLOR and current_color not in [CORRECT_COLOR, PRESENT_COLOR]:
                gw.set_key_color(s[i], MISSING_COLOR)
        
        # Check for win condition
        if s == target_word:
            gw.show_message("Congratulations! You've guessed the word!")
        else:
            if current_row == N_ROWS - 1:
                gw.show_message(f"Game over! The word was {target_word}.")
            else:
                gw.set_current_row(current_row + 1)
    
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()