# Your code for Milestone 1: Initialize the beehive with the letters in the puzzle field

from SpellingBeeGraphics import SpellingBeeGraphics

def puzzle_action(s):
    puzzle = sbg.get_field("Puzzle")
    
    # Check if the puzzle is legal
    if len(puzzle) != 7:
        sbg.show_message("Puzzle must have exactly 7 characters", "Red")
        return
    elif not puzzle.isalpha() or len(set(puzzle)) != 7:
        sbg.show_message("Puzzle must consist of 7 unique letters", "Red")
        return
    
    # Set beehive letters
    sbg.set_beehive_letters(puzzle)

# Startup code
sbg = SpellingBeeGraphics()
sbg.add_field("Puzzle", puzzle_action)
sbg.add_button("Solve", solve_action)