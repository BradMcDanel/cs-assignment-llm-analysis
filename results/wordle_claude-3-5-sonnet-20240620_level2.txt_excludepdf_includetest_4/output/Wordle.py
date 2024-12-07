import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    def enter_action(s):
        guess = s.upper()
        
        if guess not in [word.upper() for word in FIVE_LETTER_WORDS]:
            gw.show_message("Not in word list")
            return
        
        row = gw.get_current_row()
        
        # Check if guess matches hidden word
        if guess == hidden_word:
            for col in range(N_COLS):
                gw.set_square_color(row, col, CORRECT_COLOR)
                gw.set_key_color(guess[col], CORRECT_COLOR)
            gw.show_message("Congratulations!")
            return
        
        # Color the boxes and keys
        word_chars = list(hidden_word)
        for col in range(N_COLS):
            letter = guess[col]
            if letter == hidden_word[col]:
                gw.set_square_color(row, col, CORRECT_COLOR)
                gw.set_key_color(letter, CORRECT_COLOR)
                word_chars[col] = None
            elif letter not in word_chars:
                gw.set_square_color(row, col, MISSING_COLOR)
                if gw.get_key_color(letter) == "":
                    gw.set_key_color(letter, MISSING_COLOR)
        
        for col in range(N_COLS):
            letter = guess[col]
            if gw.get_square_color(row, col) == "":
                if letter in word_chars:
                    gw.set_square_color(row, col, PRESENT_COLOR)
                    if gw.get_key_color(letter) != CORRECT_COLOR:
                        gw.set_key_color(letter, PRESENT_COLOR)
                    word_chars[word_chars.index(letter)] = None
                else:
                    gw.set_square_color(row, col, MISSING_COLOR)
                    if gw.get_key_color(letter) == "":
                        gw.set_key_color(letter, MISSING_COLOR)
        
        if row == N_ROWS - 1:
            gw.show_message(f"The word was {hidden_word}")
        else:
            gw.set_current_row(row + 1)

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    hidden_word = random.choice(FIVE_LETTER_WORDS).upper()
    
    N_ROWS = 6
    N_COLS = 5

# Startup code

if __name__ == "__main__":
    wordle()