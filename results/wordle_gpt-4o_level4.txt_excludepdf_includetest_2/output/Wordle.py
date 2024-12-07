import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, N_ROWS, N_COLS

def wordle():
    def enter_action(s):
        nonlocal current_row
        guess = s.strip().lower()
        if guess not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return
        
        # Check if the guess matches the hidden word
        correct = True
        hidden_word = gw.get_square_letter(current_row, 0).lower()
        letter_count = {}
        
        # Calculate letter frequency in hidden word
        for letter in hidden_word:
            letter_count[letter] = letter_count.get(letter, 0) + 1

        # First pass: mark correct positions
        for col in range(N_COLS):
            guessed_letter = guess[col]
            if guessed_letter == hidden_word[col]:
                gw.set_square_color(current_row, col, CORRECT_COLOR)
                letter_count[guessed_letter] -= 1
            else:
                correct = False

        # Second pass: mark present letters
        for col in range(N_COLS):
            guessed_letter = guess[col]
            if gw.get_square_color(current_row, col) != CORRECT_COLOR:
                if letter_count.get(guessed_letter, 0) > 0:
                    gw.set_square_color(current_row, col, PRESENT_COLOR)
                    letter_count[guessed_letter] -= 1
                else:
                    gw.set_square_color(current_row, col, MISSING_COLOR)

        # Update the virtual keyboard
        for letter in guess:
            current_color = gw.get_key_color(letter)
            new_color = MISSING_COLOR
            if letter in hidden_word:
                new_color = PRESENT_COLOR
                if hidden_word.count(letter) == guess.count(letter):
                    new_color = CORRECT_COLOR
            if current_color != CORRECT_COLOR:  # Once a letter is marked correct, it shouldn't change
                gw.set_key_color(letter, new_color)

        if correct and guess == hidden_word:
            gw.show_message("Congratulations! You've guessed the word!")
        else:
            current_row += 1
            if current_row >= N_ROWS:
                gw.show_message(f"Sorry, you've run out of guesses. The word was '{hidden_word.upper()}'.")

    gw = WordleGWindow()
    current_row = 0
    hidden_word = random.choice(FIVE_LETTER_WORDS).upper()

    # Display the hidden word in the first row for milestone 1
    for col in range(N_COLS):
        gw.set_square_letter(0, col, hidden_word[col])

    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()