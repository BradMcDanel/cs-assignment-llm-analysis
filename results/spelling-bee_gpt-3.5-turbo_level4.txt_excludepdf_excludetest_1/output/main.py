from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

# Starter program
def spelling_bee():
    def puzzle_action(s):
        puzzle = sbg.get_field("Puzzle")
        if is_legal_puzzle(puzzle):
            sbg.set_beehive_letters(puzzle.upper())
        else:
            sbg.show_message("Invalid puzzle. Please enter exactly seven unique alphabetic characters.", "Red")

    def solve_action(s):
        dictionary = read_dictionary(DICTIONARY_FILE)
        puzzle_letters = sbg.get_beehive_letters()
        for word in dictionary:
            if is_legal_word(word, puzzle_letters):
                sbg.add_word(word, "Blue" if is_pangram(word, puzzle_letters) else "Black")

    def is_legal_puzzle(puzzle):
        return len(puzzle) == 7 and len(set(puzzle)) == 7 and puzzle.isalpha()

    def read_dictionary(file_name):
        with open(file_name, 'r') as file:
            return [word.strip().lower() for word in file]

    def is_legal_word(word, puzzle_letters):
        return len(word) >= 4 and all(letter in puzzle_letters for letter in word) and puzzle_letters[0] in word

    def is_pangram(word, puzzle_letters):
        return all(letter in word for letter in puzzle_letters)

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

if __name__ == "__main__":
    spelling_bee()