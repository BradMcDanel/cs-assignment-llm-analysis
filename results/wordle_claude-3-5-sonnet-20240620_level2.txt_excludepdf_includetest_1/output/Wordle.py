import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    def enter_action(s):
        guess = s.upper()
        
        if guess.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return
        
        # Check guess against secret word
        for i in range(5):
            letter = guess[i]
            if letter == secret_word[i]:
                gw.set_square_color(current_row, i, CORRECT_COLOR)
                gw.set_key_color(letter, CORRECT_COLOR)
            elif letter in secret_word:
                gw.set_square_color(current_row, i, PRESENT_COLOR)
                if gw.get_key_color(letter) != CORRECT_COLOR:
                    gw.set_key_color(letter, PRESENT_COLOR)
            else:
                gw.set_square_color(current_row, i, MISSING_COLOR)
                gw.set_key_color(letter, MISSING_COLOR)
        
        if guess == secret_word:
            gw.show_message("Congratulations!")
        elif current_row == 5:
            gw.show_message(f"The word was {secret_word}")
        else:
            gw.set_current_row(current_row + 1)

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    secret_word = random.choice(FIVE_LETTER_WORDS).upper()
    current_row = 0

# Startup code
if __name__ == "__main__":
    wordle()