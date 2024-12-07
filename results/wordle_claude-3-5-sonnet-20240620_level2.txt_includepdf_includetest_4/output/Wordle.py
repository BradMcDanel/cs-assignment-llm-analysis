import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    def enter_action(s):
        s = s.lower()
        if s not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return
        
        gw.show_message("")
        
        # Check letters and update colors
        for i in range(N_COLS):
            letter = s[i]
            if letter == hidden_word[i]:
                gw.set_square_color(current_row, i, CORRECT_COLOR)
                gw.set_key_color(letter.upper(), CORRECT_COLOR)
            elif letter in hidden_word:
                gw.set_square_color(current_row, i, PRESENT_COLOR)
                if gw.get_key_color(letter.upper()) != CORRECT_COLOR:
                    gw.set_key_color(letter.upper(), PRESENT_COLOR)
            else:
                gw.set_square_color(current_row, i, MISSING_COLOR)
                gw.set_key_color(letter.upper(), MISSING_COLOR)
        
        # Check for win
        if s == hidden_word:
            gw.show_message("Congratulations!")
        else:
            nonlocal current_row
            current_row += 1
            if current_row == N_ROWS:
                gw.show_message(f"Game over. The word was {hidden_word}.")
            else:
                gw.set_current_row(current_row)

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
    
    hidden_word = random.choice(FIVE_LETTER_WORDS)
    current_row = 0
    gw.set_current_row(current_row)

# Startup code
if __name__ == "__main__":
    wordle()