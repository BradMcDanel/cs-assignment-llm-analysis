import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow

def wordle():
    def enter_action(s):
        if s.lower() in FIVE_LETTER_WORDS:  # Check if entered word is in the word list
            display_message("Word is in the word list", "green")
            color_word(s)
        else:
            display_message("Not in word list", "red")

    def display_message(msg, color):
        gw.show_message(msg, color)

    def color_word(word):
        hidden_word = random.choice(FIVE_LETTER_WORDS)
        for i, letter in enumerate(word):
            if letter == hidden_word[i]:
                gw.set_square_color(0, i, "#66BB66")  # Green for correct position
            elif letter in hidden_word:
                gw.set_square_color(0, i, "#CCBB66")  # Brownish yellow for present but incorrect position
            else:
                gw.set_square_color(0, i, "#999999")  # Gray for missing letter

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

if __name__ == "__main__":
    wordle()