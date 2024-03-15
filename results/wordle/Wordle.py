import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    target_word = random.choice(FIVE_LETTER_WORDS).upper()
    gw = WordleGWindow()
    
    def enter_action(s):
        if len(s) != N_COLS:
            gw.show_message("Incomplete guess.")
            return
        if s.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list.")
            return
        
        # Process the guess
        correct_guess = True
        used_letters = [False] * len(target_word)
        for i in range(N_COLS):
            if s[i] == target_word[i]:
                gw.set_square_color(gw.get_current_row(), i, CORRECT_COLOR)
                used_letters[i] = True
            else:
                correct_guess = False
        for i in range(N_COLS):
            if gw.get_square_color(gw.get_current_row(), i) != CORRECT_COLOR:
                if s[i] in target_word and not used_letters[target_word.index(s[i])]:
                    gw.set_square_color(gw.get_current_row(), i, PRESENT_COLOR)
                    used_letters[target_word.index(s[i])] = True
                else:
                    gw.set_square_color(gw.get_current_row(), i, MISSING_COLOR)
        
        if correct_guess:
            gw.show_message("Congratulations!")
        elif gw.get_current_row() == N_ROWS - 1:
            gw.show_message(f"Game over. The word was {target_word}.")
        else:
            gw.set_current_row(gw.get_current_row() + 1)
    
    gw.add_enter_listener(enter_action)

if __name__ == "__main__":
    wordle()