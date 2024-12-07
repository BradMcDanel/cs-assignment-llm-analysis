from SpellingBeeGraphics import SpellingBeeGraphics

def puzzle_action(s):
    puzzle = sbg.get_field("Puzzle")
    
    if len(puzzle) != 7:
        sbg.show_message("Puzzle must contain exactly seven characters", "Red")
        return
    
    if not puzzle.isalpha() or not puzzle.isupper():
        sbg.show_message("Puzzle must contain only uppercase letters", "Red")
        return
    
    if len(set(puzzle)) != 7:
        sbg.show_message("Puzzle must not contain duplicate letters", "Red")
        return
    
    sbg.set_beehive_letters(puzzle)

# Main program
sbg = SpellingBeeGraphics()
sbg.add_field("Puzzle", puzzle_action)
sbg.add_button("Solve", solve_action)