import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    # Select a random word from the list
    secret_word = random.choice(FIVE_LETTER_WORDS).upper()
    
    def enter_action(s):
        current_row = gw.get_current_row()
        
        # Ensure the entered word is valid
        if s.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return
        
        # Color the squares according to the guess
        secret_word_list = list(secret_word)
        colors = [MISSING_COLOR] * N_COLS
        
        # First pass for correct letters
        for i in range(N_COLS):
            if s[i] == secret_word[i]:
                colors[i] = CORRECT_COLOR
                secret_word_list[i] = None  # Mark as used

        # Second pass for present letters
        for i in range(N_COLS):
            if colors[i] == CORRECT_COLOR:
                continue
            if s[i] in secret_word_list:
                colors[i] = PRESENT_COLOR
                secret_word_list[secret_word_list.index(s[i])] = None  # Mark as used

        # Set the colors and update keyboard
        for i in range(N_COLS):
            gw.set_square_color(current_row, i, colors[i])
            current_key_color = gw.get_key_color(s[i])
            if colors[i] == CORRECT_COLOR or (colors[i] == PRESENT_COLOR and current_key_color != CORRECT_COLOR):
                gw.set_key_color(s[i], colors[i])
            elif colors[i] == MISSING_COLOR and current_key_color not in [CORRECT_COLOR, PRESENT_COLOR]:
                gw.set_key_color(s[i], colors[i])

        # Check win or move to the next row
        if s == secret_word:
            gw.show_message("Congratulations! You've guessed the word!")
        elif current_row < N_ROWS - 1:
            gw.set_current_row(current_row + 1)
        else:
            gw.show_message(f"Game Over! The word was {secret_word}")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()