import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    def enter_action(guess):
        nonlocal current_row
        
        guess = guess.lower()
        
        if guess not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return
        
        # Check letters and color squares
        for col in range(N_COLS):
            letter = guess[col]
            if letter == secret_word[col]:
                gw.set_square_color(current_row, col, CORRECT_COLOR)
                gw.set_key_color(letter.upper(), CORRECT_COLOR)
            elif letter in secret_word:
                gw.set_square_color(current_row, col, PRESENT_COLOR)
                if gw.get_key_color(letter.upper()) != CORRECT_COLOR:
                    gw.set_key_color(letter.upper(), PRESENT_COLOR)
            else:
                gw.set_square_color(current_row, col, MISSING_COLOR)
                gw.set_key_color(letter.upper(), MISSING_COLOR)
        
        # Check for win
        if guess == secret_word:
            gw.show_message("Congratulations!")
        elif current_row == N_ROWS - 1:
            gw.show_message(f"The word was {secret_word.upper()}")
        else:
            current_row += 1
            gw.set_current_row(current_row)

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
    
    secret_word = random.choice(FIVE_LETTER_WORDS)
    current_row = 0

if __name__ == "__main__":
    wordle()