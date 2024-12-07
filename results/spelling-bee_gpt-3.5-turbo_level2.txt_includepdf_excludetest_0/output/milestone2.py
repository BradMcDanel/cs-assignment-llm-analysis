from SpellingBeeGraphics import SpellingBeeGraphics

def read_dictionary(file):
    with open(file, 'r') as f:
        return [word.strip().lower() for word in f]

def is_valid_word(word, puzzle):
    if len(word) < 4:
        return False
    if not all(letter in puzzle for letter in word):
        return False
    if puzzle[0] not in word:
        return False
    return True

def check_words(dictionary, puzzle):
    for word in dictionary:
        if is_valid_word(word, puzzle):
            sbg.add_word(word)

def solve_action(s):
    sbg.clear_word_list()
    puzzle = sbg.get_beehive_letters()
    dictionary = read_dictionary(DICTIONARY_FILE)
    check_words(dictionary, puzzle)

sbg = SpellingBeeGraphics()
sbg.add_field("Puzzle", puzzle_action)
sbg.add_button("Solve", solve_action)