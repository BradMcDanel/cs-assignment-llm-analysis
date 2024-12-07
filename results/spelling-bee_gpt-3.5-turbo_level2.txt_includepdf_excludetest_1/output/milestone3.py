# Your code for Milestone #3 here

def solve_action(s):
    puzzle = sbg.get_beehive_letters()
    dictionary = read_dictionary(DICTIONARY_FILE)
    total_score = 0
    words_found = 0
    for word in dictionary:
        if check_word_validity(word, puzzle):
            score = calculate_score(word)
            total_score += score
            words_found += 1
            sbg.add_word(word, get_word_color(word))
    sbg.show_message(f"Words found: {words_found}, Total score: {total_score}")

def calculate_score(word):
    if len(word) == 7:
        return len(word) + 7  # Bonus for pangram
    return len(word)

def get_word_color(word):
    if len(word) == 7:
        return "Blue"
    return "Black"