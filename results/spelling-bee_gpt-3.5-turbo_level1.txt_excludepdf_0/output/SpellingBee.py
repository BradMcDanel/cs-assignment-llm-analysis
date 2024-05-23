# File: SpellingBee.py

"""
This file is the starter file for the SpellingBee project.
BE SURE TO CHANGE THIS COMMENT WHEN YOU COMPLETE YOUR SOLUTION.
"""

from SpellingBeeGraphics import SpellingBeeGraphics

# Constants

DICTIONARY_FILE = "EnglishWords.txt"

# Starter program

def spelling_bee():

    def puzzle_action(s):
        sbg.show_message("puzzle_action is not yet implemented", "Red")

    def solve_action(s):
        sbg.show_message("solve_action is not yet implemented", "Red")

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

# Startup code

if __name__ == "__main__":
    spelling_bee()
