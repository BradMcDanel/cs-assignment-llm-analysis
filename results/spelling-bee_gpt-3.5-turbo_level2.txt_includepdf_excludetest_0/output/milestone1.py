from SpellingBeeGraphics import SpellingBeeGraphics

def puzzle_action(s):
    letters = sbg.get_field("Puzzle")
    if len(letters) != 7:
        sbg.show_message("Puzzle must contain exactly seven characters", "Red")
        return
    if not letters.isalpha():
        sbg.show_message("Puzzle must contain only alphabetic characters", "Red")
        return
    if len(set(letters)) != 7:
        sbg.show_message("Each letter can appear only once in the puzzle", "Red")
        return
    sbg.set_beehive_letters(letters.upper())

def solve_action(s):
    sbg.show_message("solve_action is not yet implemented", "Red")

sbg = SpellingBeeGraphics()
sbg.add_field("Puzzle", puzzle_action)
sbg.add_button("Solve", solve_action)