from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS

def display_random_word(gw):
    random_word = random.choice(FIVE_LETTER_WORDS)
    for i in range(N_COLS):
        gw.set_square_letter(0, i, random_word[i].upper())

gw = WordleGWindow()
display_random_word(gw)