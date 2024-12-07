from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS

def wordle():
    gw = WordleGWindow()
    word = random.choice(FIVE_LETTER_WORDS)
    
    for col in range(N_COLS):
        gw.set_square_letter(0, col, word[col])

if __name__ == "__main__":
    wordle()