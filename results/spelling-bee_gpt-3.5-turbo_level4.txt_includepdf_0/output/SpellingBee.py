from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

# Starter program
def spelling_bee():
    def puzzle_action(s):
        letters = sbg.get_field("Puzzle")
        if len(letters) != 7 or not letters.isalpha() or len(set(letters)) != 7:
            sbg.show_message("Invalid puzzle input. Please enter exactly 7 unique letters.", "Red")
        else:
            sbg.set_beehive_letters(letters.upper())

    def solve_action(s):
        sbg.show_message("solve_action is not yet implemented", "Red")

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

# Startup code
if __name__ == "__main__":
    spelling_bee()