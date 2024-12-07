import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    # Pick a random word for the game
    secret_word = random.choice(FIVE_LETTER_WORDS).upper()
    
    def enter_action(s):
        # Get the current row
        current_row = gw.get_current_row()
        
        # Check if the entered word is valid
        guess = s.strip().lower()
        if guess not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return
        
        # Color the squares
        secret_word_used = [False] * len(secret_word)
        guess_used = [False] * len(guess)
        
        # First pass: Mark correct letters
        for i in range(len(guess)):
            if guess[i] == secret_word[i]:
                gw.set_square_color(current_row, i, CORRECT_COLOR)
                secret_word_used[i] = True
                guess_used[i] = True
        
        # Second pass: Mark present letters
        for i in range(len(guess)):
            if not guess_used[i]:  # If not already marked as correct
                for j in range(len(secret_word)):
                    if not secret_word_used[j] and guess[i] == secret_word[j]:
                        gw.set_square_color(current_row, i, PRESENT_COLOR)
                        secret_word_used[j] = True
                        guess_used[i] = True
                        break
        
        # Mark missing letters
        for i in range(len(guess)):
            if not guess_used[i]:
                gw.set_square_color(current_row, i, MISSING_COLOR)
        
        # Check if the word is guessed correctly
        if guess.upper() == secret_word:
            gw.show_message("Congratulations!")
        else:
            gw.set_current_row(current_row + 1)
            if current_row + 1 == 6:
                gw.show_message(f"The word was: {secret_word.upper()}")

    # Create the graphics window
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()