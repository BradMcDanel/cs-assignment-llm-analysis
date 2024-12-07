import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, N_COLS, N_ROWS

def wordle():
    # Select a random word from the dictionary as the target word
    target_word = random.choice(FIVE_LETTER_WORDS).upper()
    gw = WordleGWindow()

    def enter_action(guess):
        if guess.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return
        
        current_row = gw.get_current_row()
        correct_positions = [False] * N_COLS

        # Color the squares based on the guess
        for i in range(N_COLS):
            letter = guess[i]
            if letter == target_word[i]:
                gw.set_square_color(current_row, i, CORRECT_COLOR)
                correct_positions[i] = True
            elif letter in target_word and not correct_positions[target_word.index(letter)]:
                gw.set_square_color(current_row, i, PRESENT_COLOR)
            else:
                gw.set_square_color(current_row, i, MISSING_COLOR)

        # Check if all letters are correct
        if all(correct_positions):
            gw.show_message("Congratulations! You've guessed the word!")
        else:
            # Move to the next row
            if current_row < N_ROWS - 1:
                gw.set_current_row(current_row + 1)
            else:
                gw.show_message(f"Game over! The word was {target_word}.")

    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()