import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow

def pick_random_word():
    return random.choice(FIVE_LETTER_WORDS)

def display_word(gw, word):
    for i in range(len(word)):
        gw.set_square_letter(0, i, word[i])

if __name__ == "__main__":
    gw = WordleGWindow()
    word = pick_random_word()
    display_word(gw, word)