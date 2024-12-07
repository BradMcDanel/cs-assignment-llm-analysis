from SpellingBeeGraphics import SpellingBeeGraphics

DICTIONARY_FILE = "EnglishWords.txt"

def puzzle_action(s):
    puzzle = sbg.get_field("Puzzle").upper()
    if validate_puzzle(puzzle):
        sbg.set_beehive_letters(puzzle)
    else:
        sbg.show_message("Invalid puzzle format. Please enter exactly seven unique letters.", "Red")

def solve_action(s):
    puzzle = sbg.get_beehive_letters().lower()
    dictionary = load_dictionary(DICTIONARY_FILE)
    for word in dictionary:
        if check_word(word, puzzle):
            sbg.add_word(word, "Black")

def load_dictionary(filename):
    with open(filename, 'r') as file:
        return [line.strip().lower() for line in file]

def validate_puzzle(puzzle):
    return len(puzzle) == 7 and len(set(puzzle)) == 7 and all(letter.isalpha() for letter in puzzle)

def check_word(word, puzzle):
    return len(word) >= 4 and all(letter in puzzle for letter in word) and puzzle[0] in word

if __name__ == "__main__":
    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)