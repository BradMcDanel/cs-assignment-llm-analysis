""" 
This file is the main program for the SpellingBee project.
"""

from SpellingBeeGraphics import SpellingBeeGraphics

DICTIONARY_FILE = "EnglishWords.txt"

def spelling_bee():
    def puzzle_action(puzzle):
        if len(puzzle) == 7 and puzzle.isalpha() and len(set(puzzle)) == 7:
            sbg.set_beehive_letters(puzzle.upper())
        else:
            sbg.show_message("Invalid puzzle format. Please enter exactly 7 unique letters.", "Red")

    def solve_action(s):
        sbg.clear_word_list()
        # Implement solving logic here

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

if __name__ == "__main__":
    spelling_bee()