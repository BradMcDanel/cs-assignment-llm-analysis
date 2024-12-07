# Your code for Milestone #1 goes here
# Remember to update the puzzle_action method to handle user input, validate the puzzle, and update the beehive with the letters.

from SpellingBeeGraphics import SpellingBeeGraphics

def spelling_bee():
    def puzzle_action(s):
        letters = sbg.get_field("Puzzle")
        # Validate the puzzle input
        if len(letters) != 7:
            sbg.show_message("Puzzle must contain exactly 7 characters", "Red")
        elif not all(char.isalpha() and char.islower() for char in letters):
            sbg.show_message("Puzzle can only contain lowercase alphabet characters", "Red")
        elif len(set(letters)) != 7:
            sbg.show_message("Each letter must be unique in the puzzle", "Red")
        else:
            sbg.set_beehive_letters(letters.upper())

    def solve_action(s):
        sbg.show_message("solve_action is not yet implemented", "Red")

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

if __name__ == "__main__":
    spelling_bee()