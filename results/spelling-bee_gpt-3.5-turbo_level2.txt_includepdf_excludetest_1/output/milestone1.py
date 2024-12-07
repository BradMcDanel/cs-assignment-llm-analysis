# Your code for Milestone #1 here

from SpellingBeeGraphics import SpellingBeeGraphics

def puzzle_action(s):
    puzzle = sbg.get_field("Puzzle")
    if check_puzzle_validity(puzzle):
        sbg.set_beehive_letters(puzzle)
    else:
        sbg.show_message("Invalid puzzle. Please enter exactly seven unique letters.", "Red")

def check_puzzle_validity(puzzle):
    if len(puzzle) != 7:
        return False
    if len(set(puzzle)) != 7:
        return False
    if not puzzle.isalpha():
        return False
    return True

sbg = SpellingBeeGraphics()
sbg.add_field("Puzzle", puzzle_action)
sbg.add_button("Solve", solve_action)