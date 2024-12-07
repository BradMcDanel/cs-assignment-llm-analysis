from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, N_COLS

def color_boxes(guess, hidden_word):
    for col, letter in enumerate(guess):
        if letter == hidden_word[col]:
            gw.set_square_color(gw.get_current_row(), col, CORRECT_COLOR)
        elif letter in hidden_word:
            gw.set_square_color(gw.get_current_row(), col, PRESENT_COLOR)
        else:
            gw.set_square_color(gw.get_current_row(), col, MISSING_COLOR)

if __name__ == "__main__":
    gw = WordleGWindow()
    hidden_word = "RELIC"
    guess = "LINGO"
    color_boxes(guess, hidden_word)