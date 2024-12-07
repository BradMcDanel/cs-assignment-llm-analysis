from SpellingBeeGraphics import SpellingBeeGraphics

def word_action(s):
    word = sbg.get_field("Word").lower()
    puzzle = sbg.get_beehive_letters()
    if word in found_words:
        sbg.show_message("You already found this word", "Red")
    elif len(word) < 4:
        sbg.show_message("Word must be at least four letters", "Red")
    elif puzzle[0] not in word:
        sbg.show_message("Word must contain the center letter", "Red")
    elif not all(letter in puzzle for letter in word):
        sbg.show_message("Word contains letters not in the puzzle", "Red")
    elif word not in dictionary:
        sbg.show_message("Word is not in the dictionary", "Red")
    else:
        score = compute_score(word)
        sbg.add_word(word + " (" + str(score) + ")")
        found_words.add(word)
        sbg.show_message("Word found. Total Words: " + str(len(found_words)) + ". Total Score: " + str(total_score))

found_words = set()
total_score = 0
sbg = SpellingBeeGraphics()
sbg.add_field("Puzzle", puzzle_action)
sbg.add_field("Word", word_action)
sbg.add_button("Solve", solve_action)