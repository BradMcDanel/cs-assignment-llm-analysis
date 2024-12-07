# Your code for Milestone #4 here

def word_action(s):
    word = sbg.get_field("Word")
    puzzle = sbg.get_beehive_letters()
    dictionary = read_dictionary(DICTIONARY_FILE)
    if word in dictionary:
        if check_word_validity(word, puzzle):
            if word not in sbg.get_word_list():
                score = calculate_score(word)
                sbg.add_word(word, get_word_color(word))
                sbg.show_message(f"Words found: {len(sbg.get_word_list())}, Total score: {sbg.get_total_score()}")
            else:
                sbg.show_message("Word already found.", "Red")
        else:
            sbg.show_message("Invalid word. Please check the rules.", "Red")
    else:
        sbg.show_message("Word not found in dictionary.", "Red")