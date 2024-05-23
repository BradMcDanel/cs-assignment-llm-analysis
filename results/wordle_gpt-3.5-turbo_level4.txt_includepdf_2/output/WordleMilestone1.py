from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle_milestone1():
    gw = WordleGWindow()
    word = random.choice(FIVE_LETTER_WORDS)
    for i in range(N_COLS):
        gw.set_square_letter(0, i, word[i])

if __name__ == "__main__":
    wordle_milestone1()