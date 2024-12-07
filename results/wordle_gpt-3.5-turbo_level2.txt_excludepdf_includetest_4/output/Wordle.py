import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow

def wordle():
    
    def enter_action(s):
        if s.lower() in FIVE_LETTER_WORDS:
            check_word(s)
        else:
            gw.show_message("Not in word list")

    def check_word(s):
        # Check if the word matches the hidden word
        hidden_word = FIVE_LETTER_WORDS[random.randint(0, len(FIVE_LETTER_WORDS) - 1)]
        if s.lower() == hidden_word:
            gw.show_message("Congratulations! You guessed the word.")
        else:
            color_squares(s, hidden_word)

    def color_squares(guess, hidden_word):
        for i in range(len(guess)):
            if guess[i] == hidden_word[i]:
                gw.set_square_color(0, i, WordleGWindow.CORRECT_COLOR)
            elif guess[i] in hidden_word:
                gw.set_square_color(0, i, WordleGWindow.PRESENT_COLOR)
            else:
                gw.set_square_color(0, i, WordleGWindow.MISSING_COLOR)

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()