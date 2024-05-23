from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR

def check_word_guess(gw, word_guess):
    if word_guess not in FIVE_LETTER_WORDS:
        gw.show_message("Not in word list")
    else:
        # Display positive message
        gw.show_message("Valid word!")

        # More logic to be added for coloring squares

def color_squares(gw, word_guess, hidden_word):
    for col, letter in enumerate(word_guess):
        if letter in hidden_word:
            if word_guess[col] == hidden_word[col]:
                gw.set_square_color(gw.get_current_row(), col, CORRECT_COLOR)
            else:
                gw.set_square_color(gw.get_current_row(), col, PRESENT_COLOR)
        else:
            gw.set_square_color(gw.get_current_row(), col, MISSING_COLOR)