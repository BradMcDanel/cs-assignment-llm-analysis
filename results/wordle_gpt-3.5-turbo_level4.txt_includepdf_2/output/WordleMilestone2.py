from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle_milestone2():
    def enter_action(s):
        if s.lower() in FIVE_LETTER_WORDS:
            gw.show_message("You entered a valid word!")
        else:
            gw.show_message("Not in word list")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

if __name__ == "__main__":
    wordle_milestone2()