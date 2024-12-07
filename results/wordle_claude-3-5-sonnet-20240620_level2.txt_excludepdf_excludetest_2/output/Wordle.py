import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    def enter_action(s):
        if s.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return
        
        # Color the boxes
        for i in range(N_COLS):
            if s[i].upper() == hidden_word[i]:
                color = CORRECT_COLOR
            elif s[i].upper() in hidden_word:
                color = PRESENT_COLOR
            else:
                color = MISSING_COLOR
            gw.set_square_color(gw.get_current_row(), i, color)
            
            # Color the keys
            key_color = gw.get_key_color(s[i].upper())
            if key_color != CORRECT_COLOR:
                if color == CORRECT_COLOR:
                    gw.set_key_color(s[i].upper(), CORRECT_COLOR)
                elif color == PRESENT_COLOR and key_color != PRESENT_COLOR:
                    gw.set_key_color(s[i].upper(), PRESENT_COLOR)
                elif color == MISSING_COLOR and key_color is None:
                    gw.set_key_color(s[i].upper(), MISSING_COLOR)
        
        if s.upper() == hidden_word:
            gw.show_message("Congratulations! You guessed the word!")
        elif gw.get_current_row() == N_ROWS - 1:
            gw.show_message(f"Game over. The word was {hidden_word}")
        else:
            gw.set_current_row(gw.get_current_row() + 1)

    N_ROWS = 6
    N_COLS = 5
    
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    hidden_word = random.choice(FIVE_LETTER_WORDS).upper()
    
    # Uncomment to display hidden word for testing
    # for i in range(N_COLS):
    #     gw.set_square_letter(0, i, hidden_word[i])

# Startup code
if __name__ == "__main__":
    wordle()