from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS

def milestone1():
    gw = WordleGWindow()
    word = random.choice(FIVE_LETTER_WORDS)
    
    for col, letter in enumerate(word):
        gw.set_square_letter(0, col, letter)

if __name__ == "__main__":
    milestone1()