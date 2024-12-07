def wordle():
    
    def enter_action(s):
        word_guess = s.lower()
        current_row = gw.get_current_row()
        
        if word_guess not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return
        
        # Color the boxes based on the guess
        used_indices = []
        for i in range(N_COLS):
            if word_guess[i] == hidden_word[i]:
                gw.set_square_color(current_row, i, CORRECT_COLOR)
                gw.set_key_color(word_guess[i].upper(), CORRECT_COLOR)
                used_indices.append(i)
        
        for i in range(N_COLS):
            if i in used_indices:
                continue
            
            if word_guess[i] in hidden_word and hidden_word.index(word_guess[i]) not in used_indices:
                gw.set_square_color(current_row, i, PRESENT_COLOR)
                if gw.get_key_color(word_guess[i].upper()) != CORRECT_COLOR:
                    gw.set_key_color(word_guess[i].upper(), PRESENT_COLOR)
                used_indices.append(hidden_word.index(word_guess[i]))
            else:
                gw.set_square_color(current_row, i, MISSING_COLOR)
                if gw.get_key_color(word_guess[i].upper()) not in [CORRECT_COLOR, PRESENT_COLOR]:
                    gw.set_key_color(word_guess[i].upper(), MISSING_COLOR)
        
        if word_guess == hidden_word:
            gw.show_message("Congratulations! You guessed the word!")
        else:
            gw.show_message("Keep guessing!")
            gw.set_current_row(current_row + 1)

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
    
    # Milestone #1 code remains unchanged