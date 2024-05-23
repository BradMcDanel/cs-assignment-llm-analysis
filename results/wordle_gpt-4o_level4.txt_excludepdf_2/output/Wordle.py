"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, N_ROWS, N_COLS

def wordle():
    def enter_action(s):
        current_row = gw.get_current_row()
        if len(s) != N_COLS:
            gw.show_message("Please enter a 5-letter word.")
            return

        guess = s.lower()
        if guess not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return
        
        # Coloring logic
        correct_word = hidden_word
        correct_word_list = list(correct_word)
        guess_list = list(guess)
        colors = [MISSING_COLOR] * N_COLS
        
        # First pass: Check for correct letters in the correct position
        for i in range(N_COLS):
            if guess_list[i] == correct_word_list[i]:
                colors[i] = CORRECT_COLOR
                correct_word_list[i] = None  # mark as used
        
        # Second pass: Check for correct letters in the wrong position
        for i in range(N_COLS):
            if colors[i] == MISSING_COLOR and guess_list[i] in correct_word_list:
                colors[i] = PRESENT_COLOR
                correct_word_list[correct_word_list.index(guess_list[i])] = None  # mark as used
        
        # Update the GUI with colors and letters
        for i in range(N_COLS):
            gw.set_square_color(current_row, i, colors[i])
            gw.set_square_letter(current_row, i, s[i])
            gw.set_key_color(s[i], colors[i])
        
        if all(color == CORRECT_COLOR for color in colors):
            gw.show_message("Congratulations! You've guessed the word!")
        elif current_row == N_ROWS - 1:
            gw.show_message(f"Sorry! The word was {hidden_word.upper()}.")
        else:
            gw.set_current_row(current_row + 1)
    
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
    
    hidden_word = random.choice(FIVE_LETTER_WORDS)
    print(f"Hidden word for debugging: {hidden_word}")  # Remove or comment out in production

# Startup code
if __name__ == "__main__":
    wordle()