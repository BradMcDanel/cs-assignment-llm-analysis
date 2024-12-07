import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    hidden_word = random.choice(FIVE_LETTER_WORDS).upper()
    gw = WordleGWindow()

    def enter_action(s):
        s = s.upper()
        if s.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return
        
        current_row = gw.get_current_row()
        colors = [MISSING_COLOR] * N_COLS
        hidden_word_chars = list(hidden_word)
        
        # First pass for correct positions
        for i in range(N_COLS):
            if s[i] == hidden_word[i]:
                colors[i] = CORRECT_COLOR
                hidden_word_chars[i] = None
        
        # Second pass for present characters
        for i in range(N_COLS):
            if colors[i] == MISSING_COLOR and s[i] in hidden_word_chars:
                colors[i] = PRESENT_COLOR
                hidden_word_chars[hidden_word_chars.index(s[i])] = None
        
        # Set colors for each box and update keyboard
        for col in range(N_COLS):
            gw.set_square_color(current_row, col, colors[col])
            current_key_color = gw.get_key_color(s[col])
            if colors[col] == CORRECT_COLOR or (colors[col] == PRESENT_COLOR and current_key_color != CORRECT_COLOR):
                gw.set_key_color(s[col], colors[col])
            elif colors[col] == MISSING_COLOR and current_key_color not in (CORRECT_COLOR, PRESENT_COLOR):
                gw.set_key_color(s[col], MISSING_COLOR)
        
        if s == hidden_word:
            gw.show_message("Congratulations!")
        else:
            gw.set_current_row(current_row + 1)

    gw.add_enter_listener(enter_action)

if __name__ == "__main__":
    wordle()