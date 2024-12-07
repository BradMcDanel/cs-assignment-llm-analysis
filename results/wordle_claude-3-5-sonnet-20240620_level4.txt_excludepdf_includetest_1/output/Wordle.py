import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, N_ROWS, N_COLS

def wordle():
    # Choose a random word from the dictionary
    secret_word = random.choice(FIVE_LETTER_WORDS).upper()
    
    def enter_action(s):
        nonlocal secret_word
        current_row = gw.get_current_row()
        
        # Check if the entered word is in the dictionary
        if s.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return
        
        # Color the boxes
        word_matched = True
        used_letters = [False] * 5
        
        # First pass: mark correct letters
        for i in range(N_COLS):
            if s[i] == secret_word[i]:
                gw.set_square_color(current_row, i, CORRECT_COLOR)
                used_letters[i] = True
            else:
                word_matched = False
        
        # Second pass: mark present and missing letters
        for i in range(N_COLS):
            if s[i] != secret_word[i]:
                if s[i] in secret_word:
                    # Check if this letter hasn't been marked as correct already
                    if s[i] in [secret_word[j] for j in range(N_COLS) if not used_letters[j]]:
                        gw.set_square_color(current_row, i, PRESENT_COLOR)
                    else:
                        gw.set_square_color(current_row, i, MISSING_COLOR)
                else:
                    gw.set_square_color(current_row, i, MISSING_COLOR)
        
        # Update key colors
        for i in range(N_COLS):
            letter = s[i]
            current_color = gw.get_key_color(letter)
            new_color = gw.get_square_color(current_row, i)
            if current_color != CORRECT_COLOR:
                if new_color == CORRECT_COLOR or (new_color == PRESENT_COLOR and current_color != PRESENT_COLOR):
                    gw.set_key_color(letter, new_color)
                elif new_color == MISSING_COLOR and current_color is None:
                    gw.set_key_color(letter, new_color)
        
        # Check if the word is guessed correctly
        if word_matched:
            gw.show_message("Congratulations!")
        else:
            # Move to the next row
            next_row = current_row + 1
            if next_row == N_ROWS:
                gw.show_message(f"Game over. The word was {secret_word}")
            else:
                gw.set_current_row(next_row)

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()