import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    hidden_word = random.choice(FIVE_LETTER_WORDS).upper()
    
    def enter_action(s):
        guess = s.strip().upper()
        if guess.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return
        
        current_row = gw.get_current_row()
        if current_row < N_ROWS:
            hidden_word_copy = list(hidden_word)
            
            for col in range(N_COLS):
                gw.set_square_letter(current_row, col, guess[col])
                if guess[col] == hidden_word[col]:
                    gw.set_square_color(current_row, col, CORRECT_COLOR)
                    hidden_word_copy[col] = None
                    gw.set_key_color(guess[col], CORRECT_COLOR)
            
            for col in range(N_COLS):
                if gw.get_square_color(current_row, col) != CORRECT_COLOR:
                    if guess[col] in hidden_word_copy:
                        gw.set_square_color(current_row, col, PRESENT_COLOR)
                        hidden_word_copy[hidden_word_copy.index(guess[col])] = None
                        if gw.get_key_color(guess[col]) != CORRECT_COLOR:
                            gw.set_key_color(guess[col], PRESENT_COLOR)
                    else:
                        gw.set_square_color(current_row, col, MISSING_COLOR)
                        if gw.get_key_color(guess[col]) not in [CORRECT_COLOR, PRESENT_COLOR]:
                            gw.set_key_color(guess[col], MISSING_COLOR)
            
            if guess == hidden_word:
                gw.show_message("Congratulations!")
            else:
                gw.set_current_row(current_row + 1)
    
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()