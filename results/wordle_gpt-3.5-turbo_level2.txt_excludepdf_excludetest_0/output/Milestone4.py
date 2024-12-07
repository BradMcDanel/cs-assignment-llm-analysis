from WordleGraphics import WordleGWindow, CORRECT_COLOR, N_COLS

def color_keys(guess, hidden_word):
    for letter in guess:
        for col in range(N_COLS):
            if letter == hidden_word[col]:
                gw.set_key_color(letter, CORRECT_COLOR)

if __name__ == "__main__":
    gw = WordleGWindow()
    hidden_word = "RELIC"
    guess = "LINGO"
    color_keys(guess, hidden_word)