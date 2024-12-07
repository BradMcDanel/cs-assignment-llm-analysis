from SpellingBeeGraphics import SpellingBeeGraphics

def spelling_bee():
    def puzzle_action(s):
        puzzle = sbg.get_field("Puzzle")
        if is_legal_puzzle(puzzle):
            sbg.set_beehive_letters(puzzle.upper())
        else:
            sbg.show_message("Invalid puzzle. Please enter exactly 7 unique letters.", "Red")

    def is_legal_puzzle(puzzle):
        return len(puzzle) == 7 and len(set(puzzle)) == 7 and puzzle.isalpha()

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

if __name__ == "__main__":
    spelling_bee()