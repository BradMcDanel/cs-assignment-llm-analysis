import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    gw = WordleGWindow()
    
    # Choose a random word
    secret_word = random.choice(FIVE_LETTER_WORDS).upper()
    
    def enter_action(guess):
        guess = guess.lower()
        
        if guess not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return
        
        # Color the boxes
        for i in range(N_COLS):
            if guess[i] == secret_word[i].lower():
                gw.set_square_color(gw.get_current_row(), i, CORRECT_COLOR)
                gw.set_key_color(guess[i].upper(), CORRECT_COLOR)
            elif guess[i] in secret_word.lower():
                gw.set_square_color(gw.get_current_row(), i, PRESENT_COLOR)
                if gw.get_key_color(guess[i].upper()) != CORRECT_COLOR:
                    gw.set_key_color(guess[i].upper(), PRESENT_COLOR)
            else:
                gw.set_square_color(gw.get_current_row(), i, MISSING_COLOR)
                gw.set_key_color(guess[i].upper(), MISSING_COLOR)
        
        if guess == secret_word.lower():
            gw.show_message("Congratulations!")
        elif gw.get_current_row() == N_ROWS - 1:
            gw.show_message(f"The word was {secret_word}")
        else:
            gw.set_current_row(gw.get_current_row() + 1)

    gw.add_enter_listener(enter_action)

if __name__ == "__main__":
    wordle()