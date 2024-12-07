import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, N_ROWS, N_COLS

def wordle():
    def enter_action(s):
        word = ""
        for col in range(N_COLS):
            word += gw.get_square_letter(gw.get_current_row(), col)
        
        word = word.lower()
        
        if word not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return
        
        # Check letters and color the boxes
        for col in range(N_COLS):
            letter = word[col]
            if letter == hidden_word[col]:
                color = CORRECT_COLOR
            elif letter in hidden_word:
                color = PRESENT_COLOR
            else:
                color = MISSING_COLOR
            
            gw.set_square_color(gw.get_current_row(), col, color)
            
            # Update key color
            current_key_color = gw.get_key_color(letter.upper())
            if current_key_color != CORRECT_COLOR:
                if color == CORRECT_COLOR or (color == PRESENT_COLOR and current_key_color != PRESENT_COLOR):
                    gw.set_key_color(letter.upper(), color)
                elif color == MISSING_COLOR and current_key_color is None:
                    gw.set_key_color(letter.upper(), color)
        
        if word == hidden_word:
            gw.show_message("Congratulations!")
        elif gw.get_current_row() == N_ROWS - 1:
            gw.show_message(f"The word was: {hidden_word.upper()}")
        else:
            gw.set_current_row(gw.get_current_row() + 1)

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    # Choose a random word
    hidden_word = random.choice(FIVE_LETTER_WORDS)
    
    # For testing purposes, display the hidden word in the first row
    for col, letter in enumerate(hidden_word.upper()):
        gw.set_square_letter(0, col, letter)

# Startup code
if __name__ == "__main__":
    wordle()