from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

# Global variables
words_list = []

def read_dictionary():
    with open(DICTIONARY_FILE, 'r') as file:
        words_list = [line.strip().lower() for line in file]

def is_valid_word(word, puzzle_letters):
    if len(word) < 4:
        return False
    if not all(char in puzzle_letters for char in word):
        return False
    if puzzle_letters[0] not in word:
        return False
    if word.lower() not in words_list:
        return False
    return True

def solve_puzzle(puzzle_letters):
    for word in words_list:
        if is_valid_word(word, puzzle_letters):
            sbg.add_word(word, "Black")

def solve_action(s):
    puzzle_letters = sbg.get_beehive_letters()
    sbg.clear_word_list()
    solve_puzzle(puzzle_letters)

def spelling_bee():
    read_dictionary()

    def puzzle_action(s):
        user_input = sbg.get_field("Puzzle")
        if len(user_input) != 7 or not user_input.isalpha() or len(set(user_input)) != 7:
            sbg.show_message("Invalid puzzle. Please enter exactly 7 unique letters.", "Red")
        else:
            sbg.set_beehive_letters(user_input.upper())

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

if __name__ == "__main__":
    spelling_bee()