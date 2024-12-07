from SpellingBeeGraphics import SpellingBeeGraphics

def load_dictionary(file):
    with open(file, 'r') as f:
        return set(word.strip() for word in f)

def check_word(word, puzzle):
    center_letter = puzzle[0]
    return len(word) >= 4 and center_letter in word and all(letter in puzzle for letter in word)

def solve_action(s):
    puzzle = sbg.get_beehive_letters()
    dictionary = load_dictionary(DICTIONARY_FILE)
    for word in dictionary:
        if check_word(word, puzzle):
            sbg.add_word(word)

sbg = SpellingBeeGraphics()
sbg.add_field("Puzzle", lambda s: sbg.set_beehive_letters(s.upper()))
sbg.add_button("Solve", solve_action)