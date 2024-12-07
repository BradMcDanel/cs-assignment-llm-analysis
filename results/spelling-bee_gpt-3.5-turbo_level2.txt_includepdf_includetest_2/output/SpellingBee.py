# File: SpellingBee.py

from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

# Starter program
def spelling_bee():
    def puzzle_action(s):
        puzzle = sbg.get_field("Puzzle")
        if len(puzzle) == 7 and puzzle.isalpha() and len(set(puzzle)) == 7:
            sbg.set_beehive_letters(puzzle.upper())
        else:
            sbg.show_message("Invalid puzzle. Please enter exactly seven unique alphabetic characters.", "Red")

    def solve_action(s):
        sbg.clear_word_list()
        puzzle_letters = sbg.get_beehive_letters()
        with open(DICTIONARY_FILE, 'r') as file:
            words = [word.strip() for word in file.readlines()]
            for word in words:
                if len(word) >= 4 and all(char in puzzle_letters for char in word) and puzzle_letters[0] in word:
                    sbg.add_word(word)
        sbg.show_message(f"Found {len(words)} words.", "Black")

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

# Startup code
if __name__ == "__main__":
    spelling_bee()