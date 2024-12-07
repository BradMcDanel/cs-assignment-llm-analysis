from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

# Starter program
def spelling_bee():
    def puzzle_action(s):
        puzzle = sbg.get_field("Puzzle")
        if validate_puzzle(puzzle):
            sbg.set_beehive_letters(puzzle)
        else:
            sbg.show_message("Invalid puzzle format", "Red")

    def solve_action(s):
        beehive_letters = sbg.get_beehive_letters()
        if beehive_letters:
            solve_puzzle(beehive_letters)

    def validate_puzzle(puzzle):
        if len(puzzle) != 7:
            return False
        if not puzzle.isalpha() or len(set(puzzle)) != 7:
            return False
        return True

    def solve_puzzle(beehive_letters):
        dictionary = read_dictionary(DICTIONARY_FILE)
        center_letter = beehive_letters[0]
        for word in dictionary:
            if len(word) >= 4 and all(letter in beehive_letters for letter in word) and center_letter in word:
                sbg.add_word(word)
    
    def read_dictionary(filename):
        with open(filename, 'r') as file:
            return [line.strip() for line in file]

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

if __name__ == "__main__":
    spelling_bee()