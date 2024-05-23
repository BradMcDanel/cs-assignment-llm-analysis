import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, N_ROWS, N_COLS

def wordle():
    def enter_action(s):
        nonlocal current_word
        current_row = gw.get_current_row()
        guess = ''.join([gw.get_square_letter(current_row, col) for col in range(N_COLS)]).lower()

        if guess not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return

        for col in range(N_COLS):
            letter = guess[col]
            if letter == current_word[col]:
                gw.set_square_color(current_row, col, CORRECT_COLOR)
            elif letter in current_word:
                gw.set_square_color(current_row, col, PRESENT_COLOR)
            else:
                gw.set_square_color(current_row, col, MISSING_COLOR)
            gw.set_key_color(letter.upper(), gw.get_square_color(current_row, col))

        if guess == current_word:
            gw.show_message("Congratulations! You've guessed the word!")
        elif current_row == N_ROWS - 1:
            gw.show_message(f"Game Over! The word was {current_word.upper()}.")
        else:
            gw.set_current_row(current_row + 1)

    gw = WordleGWindow()
    current_word = random.choice(FIVE_LETTER_WORDS)

    for col in range(N_COLS):
        gw.set_square_letter(0, col, current_word[col].upper())

    gw.add_enter_listener(enter_action)

if __name__ == "__main__":
    wordle()