from SpellingBeeGraphics import SpellingBeeGraphics

def puzzle_action(s):
    puzzle = sbg.get_field("Puzzle")
    if len(puzzle) != 7:
        sbg.show_message("Puzzle must contain exactly 7 characters", "Red")
    elif not puzzle.isalpha() or len(set(puzzle)) != 7:
        sbg.show_message("Invalid characters in the puzzle or characters are repeated", "Red")
    else:
        sbg.set_beehive_letters(puzzle.upper())

sbg = SpellingBeeGraphics()
sbg.add_field("Puzzle", puzzle_action)
sbg.add_button("Solve", lambda s: sbg.show_message("solve_action is not yet implemented", "Red"))