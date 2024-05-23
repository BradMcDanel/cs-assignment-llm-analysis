from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle_milestone4():
    def enter_action(s):
        if s.lower() in FIVE_LETTER_WORDS:
            # Logic to color the boxes based on correctness of letters
            pass
        else:
            gw.show_message("Not in word list")
    
    def update_key_colors():
        # Logic to update key colors based on user input
        pass

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
    update_key_colors()

if __name__ == "__main__":
    wordle_milestone4()