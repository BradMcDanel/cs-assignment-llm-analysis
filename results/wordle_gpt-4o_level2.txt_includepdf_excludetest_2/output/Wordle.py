import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    # Choose a random word from the list
    secret_word = random.choice(FIVE_LETTER_WORDS).upper()
    
    def enter_action(guess):
        current_row = gw.get_current_row()
        
        # Check if the entered word is in the dictionary
        if guess.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return

        # Check each letter and color the boxes
        used_positions = [False] * N_COLS
        for i in range(N_COLS):
            letter = guess[i]
            if letter == secret_word[i]:
                gw.set_square_color(current_row, i, CORRECT_COLOR)
                gw.set_key_color(letter, CORRECT_COLOR)
                used_positions[i] = True
            elif letter in secret_word and not used_positions[secret_word.index(letter)]:
                gw.set_square_color(current_row, i, PRESENT_COLOR)
                if gw.get_key_color(letter) != CORRECT_COLOR:
                    gw.set_key_color(letter, PRESENT_COLOR)
            else:
                gw.set_square_color(current_row, i, MISSING_COLOR)
                if gw.get_key_color(letter) not in [CORRECT_COLOR, PRESENT_COLOR]:
                    gw.set_key_color(letter, MISSING_COLOR)

        # Check if the guessed word matches the secret word
        if guess == secret_word:
            gw.show_message("Congratulations! You've guessed the word!")
        else:
            # Move to the next row
            if current_row < N_ROWS - 1:
                gw.set_current_row(current_row + 1)
            else:
                gw.show_message(f"Game Over! The word was: {secret_word}")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()