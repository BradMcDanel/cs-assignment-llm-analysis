import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    # Pick a random word from the dictionary to be the hidden word
    hidden_word = random.choice(FIVE_LETTER_WORDS).upper()

    def enter_action(s):
        # Get the current row
        row = gw.get_current_row()

        # Check if the entered word is in the dictionary
        if s.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return

        # Color the squares based on the entered word
        used = [False] * N_COLS
        hidden_word_counts = {char: hidden_word.count(char) for char in set(hidden_word)}

        # First, mark correct positions
        for i in range(N_COLS):
            letter = s[i]
            if letter == hidden_word[i]:
                gw.set_square_color(row, i, CORRECT_COLOR)
                gw.set_key_color(letter, CORRECT_COLOR)
                used[i] = True
                hidden_word_counts[letter] -= 1

        # Then, mark present but misplaced letters
        for i in range(N_COLS):
            if not used[i]:
                letter = s[i]
                if letter in hidden_word and hidden_word_counts[letter] > 0:
                    gw.set_square_color(row, i, PRESENT_COLOR)
                    if gw.get_key_color(letter) != CORRECT_COLOR:  # Don't overwrite a correct mark
                        gw.set_key_color(letter, PRESENT_COLOR)
                    hidden_word_counts[letter] -= 1
                else:
                    gw.set_square_color(row, i, MISSING_COLOR)
                    if gw.get_key_color(letter) not in [CORRECT_COLOR, PRESENT_COLOR]:  # Only set if not correctly identified
                        gw.set_key_color(letter, MISSING_COLOR)

        # Check if the guess is correct
        if s == hidden_word:
            gw.show_message("Congratulations! You've guessed the word.")
        elif row == N_ROWS - 1:
            gw.show_message(f"Game over! The word was {hidden_word}.")
        else:
            # Move to next row
            gw.set_current_row(row + 1)

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()