import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    # Select a random word from the dictionary
    target_word = random.choice(FIVE_LETTER_WORDS).upper()
    gw = WordleGWindow()

    def enter_action(guess):
        current_row = gw.get_current_row()
        
        # Check if the guess is a legal word
        if guess.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return
        
        # Check and color the squares based on the guess
        used_letters = [False] * N_COLS
        for i in range(N_COLS):
            if guess[i] == target_word[i]:
                gw.set_square_color(current_row, i, CORRECT_COLOR)
                gw.set_key_color(guess[i], CORRECT_COLOR)
                used_letters[i] = True
            else:
                gw.set_square_color(current_row, i, MISSING_COLOR)
        
        for i in range(N_COLS):
            if not used_letters[i] and guess[i] in target_word:
                if target_word.count(guess[i]) > guess[:i].count(guess[i]):
                    gw.set_square_color(current_row, i, PRESENT_COLOR)
                    if gw.get_key_color(guess[i]) != CORRECT_COLOR:
                        gw.set_key_color(guess[i], PRESENT_COLOR)

        # Check for a win
        if guess == target_word:
            gw.show_message("Congratulations! You've guessed the word!")
        else:
            gw.set_current_row(current_row + 1)
            if current_row == N_ROWS - 1:
                gw.show_message(f"Game Over! The word was {target_word}")

    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()