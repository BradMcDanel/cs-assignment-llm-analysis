from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

# Read dictionary file into a list
def read_dictionary():
    with open(DICTIONARY_FILE, 'r') as file:
        dictionary = [word.strip().lower() for word in file]
    return dictionary

# Check if a word meets the requirements
def is_valid_word(word, puzzle):
    if len(word) < 4:
        return False
    if len(set(word) - set(puzzle)) > 0:
        return False
    if puzzle[0] not in word:
        return False
    return True

# Solve the Spelling Bee puzzle
def solve_action(s):
    dictionary = read_dictionary()
    puzzle = s.get_beehive_letters()
    for word in dictionary:
        if is_valid_word(word, puzzle):
            s.add_word(word, "Black")

def spelling_bee():
    def puzzle_action(s):
        puzzle = s.get_field("Puzzle")
        if len(puzzle) != 7 or not puzzle.isalpha() or len(set(puzzle)) != 7:
            s.show_message("Invalid puzzle. Please enter 7 unique letters.", "Red")
        else:
            s.set_beehive_letters(puzzle.upper())

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

if __name__ == "__main__":
    spelling_bee()