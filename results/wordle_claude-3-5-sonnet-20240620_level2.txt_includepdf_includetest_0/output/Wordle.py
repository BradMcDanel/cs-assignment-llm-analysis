import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    def enter_action(s):
        nonlocal current_row
        
        if s.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return
        
        # Check letters and update colors
        for i in range(N_COLS):
            letter = s[i]
            if letter == target_word[i]:
                gw.set_square_color(current_row, i, CORRECT_COLOR)
                gw.set_key_color(letter, CORRECT_COLOR)
            elif letter in target_word:
                gw.set_square_color(current_row, i, PRESENT_COLOR)
                if gw.get_key_color(letter) != CORRECT_COLOR:
                    gw.set_key_color(letter, PRESENT_COLOR)
            else:
                gw.set_square_color(current_row, i, MISSING_COLOR)
                if gw.get_key_color(letter) == MISSING_COLOR:
                    gw.set_key_color(letter, MISSING_COLOR)
        
        # Check win condition
        if s == target_word:
            gw.show_message("Congratulations!")
        elif current_row == N_ROWS - 1:
            gw.show_message(f"Game over. The word was {target_word}")
        else:
            current_row += 1
            gw.set_current_row(current_row)

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
    
    target_word = random.choice(FIVE_LETTER_WORDS).upper()
    current_row = 0

# Startup code
if __name__ == "__main__":
    wordle()