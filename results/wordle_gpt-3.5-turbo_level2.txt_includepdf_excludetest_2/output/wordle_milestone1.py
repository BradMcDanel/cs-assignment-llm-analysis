from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS

def wordle():

    def enter_action(s):
        gw.show_message("You have to implement this method.")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
    
    # Milestone 1: Pick a random word and display it in the first row of boxes
    word = random.choice(FIVE_LETTER_WORDS)
    for col in range(N_COLS):
        gw.set_square_letter(0, col, word[col])

# Startup code

if __name__ == "__main__":
    wordle()