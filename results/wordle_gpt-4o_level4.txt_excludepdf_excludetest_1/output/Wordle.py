import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, N_ROWS, N_COLS

def wordle():

    def enter_action(s):
        if s.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return
        
        current_row = gw.get_current_row()
        word_to_guess = "".join([gw.get_square_letter(0, col) for col in range(N_COLS)])
        
        used_letters = [False] * N_COLS
        
        # First pass: Check for correct positions
        for i in range(N_COLS):
            if s[i].lower() == word_to_guess[i]:
                gw.set_square_color(current_row, i, CORRECT_COLOR)
                gw.set_key_color(s[i], CORRECT_COLOR)
                used_letters[i] = True
            else:
                gw.set_square_color(current_row, i, MISSING_COLOR)
        
        # Second pass: Check for present but misplaced letters
        for i in range(N_COLS):
            if not used_letters[i] and s[i].lower() in word_to_guess:
                for j in range(N_COLS):
                    if s[i].lower() == word_to_guess[j] and s[i] != gw.get_square_letter(current_row, j):
                        gw.set_square_color(current_row, i, PRESENT_COLOR)
                        if gw.get_key_color(s[i]) != CORRECT_COLOR:
                            gw.set_key_color(s[i], PRESENT_COLOR)
                        used_letters[j] = True
                        break
        
        if s.lower() == word_to_guess:
            gw.show_message("Congratulations! You guessed the word.")
        elif current_row + 1 < N_ROWS:
            gw.set_current_row(current_row + 1)
        else:
            gw.show_message(f"Game Over! The word was {word_to_guess.upper()}.")

    gw = WordleGWindow()
    
    # Pick a random word from the list
    word_to_guess = random.choice(FIVE_LETTER_WORDS)
    
    # Display the chosen word in the first row of boxes for testing purposes
    for col in range(N_COLS):
        gw.set_square_letter(0, col, word_to_guess[col].upper())
    
    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()