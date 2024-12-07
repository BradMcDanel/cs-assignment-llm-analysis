import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    # Select a random hidden word
    hidden_word = random.choice(FIVE_LETTER_WORDS).upper()
    
    def enter_action(s):
        word_entered = s.upper()
        current_row = gw.get_current_row()
        
        if len(word_entered) == N_COLS and word_entered.lower() in FIVE_LETTER_WORDS:
            # Check each letter and color the box accordingly
            hidden_word_letters = list(hidden_word)
            guess_result = [MISSING_COLOR] * N_COLS

            # First pass: check for correct letters
            for i in range(N_COLS):
                if word_entered[i] == hidden_word[i]:
                    guess_result[i] = CORRECT_COLOR
                    hidden_word_letters[i] = None  # Mark as used

            # Second pass: check for present letters
            for i in range(N_COLS):
                if guess_result[i] != CORRECT_COLOR and word_entered[i] in hidden_word_letters:
                    guess_result[i] = PRESENT_COLOR
                    hidden_word_letters[hidden_word_letters.index(word_entered[i])] = None  # Mark as used

            # Set the colors for the row
            for i in range(N_COLS):
                gw.set_square_letter(current_row, i, word_entered[i])
                gw.set_square_color(current_row, i, guess_result[i])
                # Update key colors
                current_key_color = gw.get_key_color(word_entered[i])
                if current_key_color != CORRECT_COLOR:
                    gw.set_key_color(word_entered[i], guess_result[i])
            
            # Move to the next row
            gw.set_current_row(current_row + 1)
        else:
            gw.show_message("Not in word list")
    
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()