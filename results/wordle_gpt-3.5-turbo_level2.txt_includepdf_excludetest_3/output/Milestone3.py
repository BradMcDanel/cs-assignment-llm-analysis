# Your code for Milestone #3: Color the boxes

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def milestone3():
    
    def enter_action(s):
        if s.lower() in FIVE_LETTER_WORDS:
            for col in range(N_COLS):
                if s[col] == word[col]:
                    gw.set_square_color(gw.get_current_row(), col, CORRECT_COLOR)
                elif s[col] in word:
                    gw.set_square_color(gw.get_current_row(), col, PRESENT_COLOR)
                else:
                    gw.set_square_color(gw.get_current_row(), col, MISSING_COLOR)
    
    word = random.choice(FIVE_LETTER_WORDS)
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

if __name__ == "__main__":
    milestone3()