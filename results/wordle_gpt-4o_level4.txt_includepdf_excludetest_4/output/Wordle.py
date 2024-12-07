import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    # Select a random word from the dictionary
    secret_word = random.choice(FIVE_LETTER_WORDS)
    
    def enter_action(s):
        current_row = gw.get_current_row()
        
        # Check if the word is valid
        if s.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return
        
        # Determine the colors for each letter
        secret_word_counts = {letter: secret_word.count(letter) for letter in secret_word}
        result_colors = [MISSING_COLOR] * N_COLS
        
        # First pass: find correct letters
        for i in range(N_COLS):
            if s[i].lower() == secret_word[i]:
                result_colors[i] = CORRECT_COLOR
                secret_word_counts[s[i].lower()] -= 1

        # Second pass: find present but misplaced letters
        for i in range(N_COLS):
            if result_colors[i] == MISSING_COLOR and s[i].lower() in secret_word_counts and secret_word_counts[s[i].lower()] > 0:
                result_colors[i] = PRESENT_COLOR
                secret_word_counts[s[i].lower()] -= 1
        
        # Set colors for the squares and keys
        for i in range(N_COLS):
            gw.set_square_color(current_row, i, result_colors[i])
            gw.set_key_color(s[i], result_colors[i])
        
        # Check for win condition
        if all(color == CORRECT_COLOR for color in result_colors):
            gw.show_message("Congratulations! You've guessed the word!")
            return
        
        # Move to the next row
        gw.set_current_row(current_row + 1)
        # Check for game over
        if current_row + 1 >= N_ROWS:
            gw.show_message(f"Game Over! The word was '{secret_word.upper()}'")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()