import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    # Choose a random word from the dictionary
    hidden_word = random.choice(FIVE_LETTER_WORDS).upper()

    def enter_action(guess):
        # Ensure the guess is the correct length
        if len(guess) != len(hidden_word):
            gw.show_message("The word must be five letters long.")
            return
        
        # Check if the guess is in the dictionary
        if guess.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return
        
        # Check each letter and color the boxes accordingly
        current_row = gw.get_current_row()
        hidden_word_letters = list(hidden_word)
        guess_letters = list(guess)

        # First pass for correct letters
        for i in range(len(guess_letters)):
            if guess_letters[i] == hidden_word_letters[i]:
                gw.set_square_color(current_row, i, CORRECT_COLOR)
                hidden_word_letters[i] = None  # Mark this letter as used
            else:
                gw.set_square_color(current_row, i, MISSING_COLOR)
        
        # Second pass for present letters
        for i in range(len(guess_letters)):
            if gw.get_square_color(current_row, i) != CORRECT_COLOR:  # Not already colored
                if guess_letters[i] in hidden_word_letters:
                    gw.set_square_color(current_row, i, PRESENT_COLOR)
                    hidden_word_letters[hidden_word_letters.index(guess_letters[i])] = None
        
        # Update keys color
        for i in range(len(guess_letters)):
            if gw.get_square_color(current_row, i) == CORRECT_COLOR:
                gw.set_key_color(guess_letters[i], CORRECT_COLOR)
            elif gw.get_square_color(current_row, i) == PRESENT_COLOR:
                if gw.get_key_color(guess_letters[i]) != CORRECT_COLOR:
                    gw.set_key_color(guess_letters[i], PRESENT_COLOR)
            else:
                if gw.get_key_color(guess_letters[i]) not in [CORRECT_COLOR, PRESENT_COLOR]:
                    gw.set_key_color(guess_letters[i], MISSING_COLOR)
        
        # Check for win condition
        if guess == hidden_word:
            gw.show_message("Congratulations! You've guessed the word!")
        else:
            # Move to the next row if available
            if current_row < N_ROWS - 1:
                gw.set_current_row(current_row + 1)
            else:
                gw.show_message(f"Sorry! The word was {hidden_word}.")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()