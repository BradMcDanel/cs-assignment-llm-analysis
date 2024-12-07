from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, CORRECT_COLOR, KEY_COLOR

def is_valid_word(word):
    return word in FIVE_LETTER_WORDS

def check_word(word, hidden_word):
    colors = []
    for i in range(len(word)):
        if word[i] == hidden_word[i]:
            colors.append(CORRECT_COLOR)
        elif word[i] in hidden_word:
            colors.append(PRESENT_COLOR)
        else:
            colors.append(MISSING_COLOR)
    return colors

def enter_action(s):
    if not is_valid_word(s):
        gw.show_message("Not in word list")
    else:
        colors = check_word(s, hidden_word)
        for col, color in enumerate(colors):
            gw.set_square_color(gw.get_current_row(), col, color)
        gw.set_current_row(gw.get_current_row() + 1)
        
        for key in s:
            gw.set_key_color(key, KEY_COLOR)

def wordle():
    gw = WordleGWindow()
    hidden_word = random.choice(FIVE_LETTER_WORDS)
    gw.add_enter_listener(enter_action)

if __name__ == "__main__":
    wordle()