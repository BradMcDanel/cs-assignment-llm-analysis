import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    def enter_action(s):
        guess = s.strip().lower()
        if guess not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return

        current_row = gw.get_current_row()
        hidden_word_list = list(hidden_word.lower())

        # Determine the colors for each letter in the guess
        colors = [MISSING_COLOR] * N_COLS
        # First pass to check for correct letters
        for col, letter in enumerate(guess):
            if letter == hidden_word_list[col]:
                colors[col] = CORRECT_COLOR
                hidden_word_list[col] = None  # Mark this letter as used

        # Second pass to check for present letters
        for col, letter in enumerate(guess):
            if colors[col] == MISSING_COLOR and letter in hidden_word_list:
                colors[col] = PRESENT_COLOR
                hidden_word_list[hidden_word_list.index(letter)] = None  # Mark this letter as used

        # Set the colors in the grid
        for col, letter in enumerate(guess):
            gw.set_square_letter(current_row, col, letter.upper())
            gw.set_square_color(current_row, col, colors[col])
            # Update key colors
            current_key_color = gw.get_key_color(letter.upper())
            if current_key_color != CORRECT_COLOR:
                gw.set_key_color(letter.upper(), colors[col])

        # Check if the guess was correct
        if all(color == CORRECT_COLOR for color in colors):
            gw.show_message("Congratulations!")
        else:
            if current_row < N_ROWS - 1:
                gw.set_current_row(current_row + 1)
            else:
                gw.show_message(f"The word was {hidden_word}")

    # Create the Wordle graphics window
    gw = WordleGWindow()
    
    # Pick a random word from the dictionary
    hidden_word = random.choice(FIVE_LETTER_WORDS).upper()
    
    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()