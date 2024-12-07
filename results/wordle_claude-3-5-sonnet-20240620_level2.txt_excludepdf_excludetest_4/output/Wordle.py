import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    def enter_action(s):
        guess = s.upper()
        
        if guess.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return
        
        # Check letters and color squares
        for i in range(5):
            letter = guess[i]
            if letter == secret_word[i]:
                gw.set_square_color(current_row, i, CORRECT_COLOR)
                gw.set_key_color(letter, CORRECT_COLOR)
            elif letter in secret_word:
                gw.set_square_color(current_row, i, PRESENT_COLOR)
                if gw.get_key_color(letter) != CORRECT_COLOR:
                    gw.set_key_color(letter, PRESENT_COLOR)
            else:
                gw.set_square_color(current_row, i, MISSING_COLOR)
                gw.set_key_color(letter, MISSING_COLOR)
        
        nonlocal current_row
        current_row += 1
        gw.set_current_row(current_row)
        
        if guess == secret_word:
            gw.show_message("Congratulations! You guessed the word!")
        elif current_row == N_ROWS:
            gw.show_message(f"Game over. The word was {secret_word}")

    N_ROWS = 6
    N_COLS = 5
    
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    secret_word = random.choice(FIVE_LETTER_WORDS).upper()
    current_row = 0

    # Display secret word in first row (for testing)
    for i, letter in enumerate(secret_word):
        gw.set_square_letter(0, i, letter)

# Startup code
if __name__ == "__main__":
    wordle()