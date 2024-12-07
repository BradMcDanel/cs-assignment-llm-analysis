from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

# Load English words from file into a list
def load_dictionary():
    with open(DICTIONARY_FILE, 'r') as file:
        words = file.read().splitlines()
    return words

# Check if a word meets the puzzle requirements
def is_valid_word(word, puzzle):
    if len(word) < 4:
        return False
    if not all(letter in puzzle for letter in word):
        return False
    if puzzle[0] not in word:
        return False
    return True

def spelling_bee():
    dictionary = load_dictionary()

    def puzzle_action(s):
        puzzle = sbg.get_field("Puzzle")
        if len(puzzle) == 7 and all(letter.isalpha() and letter.isupper() for letter in puzzle) and len(set(puzzle)) == 7:
            sbg.set_beehive_letters(puzzle)
        else:
            sbg.show_message("Invalid puzzle format.", "Red")

    def solve_action(s):
        puzzle = sbg.get_beehive_letters()
        for word in dictionary:
            if is_valid_word(word, puzzle):
                sbg.add_word(word, "Black")

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

if __name__ == "__main__":
    spelling_bee()