import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    def enter_action(s):
        guess = s.upper()
        
        if len(guess) != 5 or guess.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return
        
        row = gw.get_current_row()
        
        # Check if guess matches secret word
        for col in range(5):
            letter = guess[col]
            if letter == secret_word[col]:
                color = CORRECT_COLOR
            elif letter in secret_word:
                color = PRESENT_COLOR
            else:
                color = MISSING_COLOR
            
            gw.set_square_color(row, col, color)
            
            # Update key color
            current_key_color = gw.get_key_color(letter)
            if current_key_color != CORRECT_COLOR:
                gw.set_key_color(letter, color)
        
        if guess == secret_word:
            gw.show_message("Congratulations!")
        elif row == 5:
            gw.show_message(f"The word was {secret_word}")
        else:
            gw.set_current_row(row + 1)

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
    
    secret_word = random.choice(FIVE_LETTER_WORDS).upper()
    
    # Uncomment to display secret word (for testing)
    # for col in range(5):
    #     gw.set_square_letter(0, col, secret_word[col])

# Startup code
if __name__ == "__main__":
    wordle()