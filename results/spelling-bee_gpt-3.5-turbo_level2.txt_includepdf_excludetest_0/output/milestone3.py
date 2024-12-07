from SpellingBeeGraphics import SpellingBeeGraphics

def compute_score(word):
    score = len(word)
    if len(word) == 7:
        score += 7  # Bonus for pangram
    return score

def solve_action(s):
    sbg.clear_word_list()
    puzzle = sbg.get_beehive_letters()
    dictionary = read_dictionary(DICTIONARY_FILE)
    total_score = 0
    word_count = 0
    for word in dictionary:
        if is_valid_word(word, puzzle):
            score = compute_score(word)
            total_score += score
            sbg.add_word(word + " (" + str(score) + ")")
            word_count += 1
    sbg.show_message("Found " + str(word_count) + " words. Total Score: " + str(total_score))

sbg = SpellingBeeGraphics()
sbg.add_field("Puzzle", puzzle_action)
sbg.add_button("Solve", solve_action)