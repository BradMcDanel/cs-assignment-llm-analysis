import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    def enter_action(s):
        if s.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return
        
        row = gw.get_current_row()
        
        # Check if guess is correct
        if s.upper() == hidden_word:
            for col in range(N_COLS):
                gw.set_square_color(row, col, CORRECT_COLOR)
                gw.set_key_color(s[col].upper(), CORRECT_COLOR)
            gw.show_message("Congratulations!")
            return
        
        # Color the boxes
        word_letters = list(hidden_word)
        for col in range(N_COLS):
            letter = s[col].upper()
            if letter == hidden_word[col]:
                gw.set_square_color(row, col, CORRECT_COLOR)
                gw.set_key_color(letter, CORRECT_COLOR)
                word_letters[col] = None
            elif letter in word_letters:
                gw.set_square_color(row, col, PRESENT_COLOR)
                if gw.get_key_color(letter) != CORRECT_COLOR:
                    gw.set_key_color(letter, PRESENT_COLOR)
                word_letters[word_letters.index(letter)] = None
            else:
                gw.set_square_color(row, col, MISSING_COLOR)
                if gw.get_key_color(letter) == None:
                    gw.set_key_color(letter, MISSING_COLOR)
        
        if row == N_ROWS - 1:
            gw.show_message(f"The word was {hidden_word}")
        else:
            gw.set_current_row(row + 1)

    N_ROWS = 6
    N_COLS = 5
    
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    hidden_word = random.choice(FIVE_LETTER_WORDS).upper()

# Startup code

if __name__ == "__main__":
    wordle()