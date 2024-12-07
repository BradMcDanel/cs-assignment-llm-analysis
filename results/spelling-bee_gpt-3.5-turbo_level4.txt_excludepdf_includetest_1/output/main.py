from SpellingBeeGraphics import SpellingBeeGraphics
from WordChecker import WordChecker

DICTIONARY_FILE = "EnglishWords.txt"

def spelling_bee():
    def puzzle_action(s):
        # Implement puzzle action functionality
        pass

    def solve_action(s):
        # Implement solve action functionality
        pass

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

if __name__ == "__main__":
    spelling_bee()