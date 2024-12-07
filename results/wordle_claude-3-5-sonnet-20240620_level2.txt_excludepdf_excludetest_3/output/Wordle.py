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
        
        gw.show_message("")
        
        # Check letters and color squares
        for col in range(N_COLS):
            letter = word[col]
            if letter == hidden_word[col]:
                color = CORRECT_COLOR
            elif letter in hidden_word:
                color = PRESENT_COLOR
            else:
                color = MISSING_COLOR
            gw.set_square_color(gw.get_current_row(), col, color)
            
            # Update key colors
            current_key_color = gw.get_key_color(letter.upper())
            if current_key_color != CORRECT_COLOR:
                if color == CORRECT_COLOR or (color == PRESENT_COLOR and current_key_color != PRESENT_COLOR):
                    gw.set_key_color(letter.upper(), color)
                elif color == MISSING_COLOR and current_key_color is None:
                    gw.set_key_color(letter.upper(), color)
        
        if word == hidden_word:
            gw.show_message("Congratulations! You've guessed the word!")
        elif gw.get_current_row() == N_ROWS - 1:
            gw.show_message(f"Game over. The word was {hidden_word.upper()}")
        else:
            gw.set_current_row(gw.get_current_row() + 1)

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
    
    hidden_word = random.choice(FIVE_LETTER_WORDS)
    
    # Uncomment the following line to display the hidden word (for testing)
    # print(f"Hidden word: {hidden_word}")

# Startup code
if __name__ == "__main__":
    wordle()