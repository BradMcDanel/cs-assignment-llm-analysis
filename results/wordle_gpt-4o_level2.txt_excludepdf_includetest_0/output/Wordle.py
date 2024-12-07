import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    secret_word = random.choice(FIVE_LETTER_WORDS)
    
    def enter_action(s):
        guess = s.lower()
        if guess not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return

        current_row = gw.get_current_row()

        secret_word_occurrences = {ch: secret_word.count(ch) for ch in set(secret_word)}
        guessed_occurrences = {ch: 0 for ch in set(secret_word)}

        # First pass for correct letters
        for i in range(N_COLS):
            if guess[i] == secret_word[i]:
                gw.set_square_color(current_row, i, CORRECT_COLOR)
                gw.set_key_color(guess[i].upper(), CORRECT_COLOR)
                guessed_occurrences[guess[i]] += 1
        
        # Second pass for present letters
        for i in range(N_COLS):
            if guess[i] != secret_word[i]:
                if guess[i] in secret_word and guessed_occurrences[guess[i]] < secret_word_occurrences[guess[i]]:
                    gw.set_square_color(current_row, i, PRESENT_COLOR)
                    if gw.get_key_color(guess[i].upper()) != CORRECT_COLOR:
                        gw.set_key_color(guess[i].upper(), PRESENT_COLOR)
                    guessed_occurrences[guess[i]] += 1
                else:
                    gw.set_square_color(current_row, i, MISSING_COLOR)
                    if gw.get_key_color(guess[i].upper()) not in (CORRECT_COLOR, PRESENT_COLOR):
                        gw.set_key_color(guess[i].upper(), MISSING_COLOR)

        # Advance to the next row
        gw.set_current_row(current_row + 1)
    
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()