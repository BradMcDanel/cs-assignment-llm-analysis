from SpellingBeeGraphics import SpellingBeeGraphics

def word_action(word):
    puzzle = sbg.get_beehive_letters()
    dictionary = read_dictionary(DICTIONARY_FILE)
    
    if word.lower() not in dictionary:
        sbg.show_message("Word not in dictionary", "Red")
    elif not all(letter in puzzle for letter in word.upper()):
        sbg.show_message("Word contains letters not in the puzzle", "Red")
    elif len(word) < 4:
        sbg.show_message("Word must be at least 4 letters long", "Red")
    elif puzzle[0] not in word.upper():
        sbg.show_message("Word must contain the center letter", "Red")
    else:
        score = calculate_score(word)
        sbg.add_word(f"{word} ({score})")
        sbg.show_message(f"Word found! Total Score: {score}")

sbg = SpellingBeeGraphics()
sbg.add_field("Puzzle", lambda s: None)
sbg.add_field("Word", word_action)
sbg.add_button("Solve", lambda s: None)