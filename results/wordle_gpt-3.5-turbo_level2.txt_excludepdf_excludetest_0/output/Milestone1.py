from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_ROWS, N_COLS

def display_random_word():
    word = random.choice(FIVE_LETTER_WORDS)
    gw = WordleGWindow()
    for col, letter in enumerate(word):
        gw.set_square_letter(0, col, letter)

if __name__ == "__main__":
    display_random_word()