from SpellingBeeGraphics import SpellingBeeGraphics

DICTIONARY_FILE = "EnglishWords.txt"

def spelling_bee():
    def puzzle_action(s):
        letters = sbg.get_field("Puzzle")
        if len(letters) != 7:
            sbg.show_message("Puzzle must contain exactly seven characters", "Red")
        elif not letters.isalpha() or len(set(letters)) != 7:
            sbg.show_message("Puzzle must contain distinct alphabetical characters only", "Red")
        else:
            sbg.set_beehive_letters(letters.upper())
            sbg.show_message("Puzzle set successfully", "Green")

    def solve_action(s):
        sbg.show_message("solve_action is not yet implemented", "Red")

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

if __name__ == "__main__":
    spelling_bee()