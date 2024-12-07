# Your code for Milestone #2 goes here
# Implement the solve_action method to check dictionary words against the puzzle rules and display legal words on the screen.

from SpellingBeeGraphics import SpellingBeeGraphics

def spelling_bee():
    def puzzle_action(s):
        sbg.show_message("puzzle_action is not yet implemented", "Red")

    def solve_action(s):
        puzzle_letters = sbg.get_beehive_letters()
        with open(DICTIONARY_FILE, 'r') as file:
            dictionary = [word.strip() for word in file.readlines()]

        for word in dictionary:
            if len(word) >= 4 and all(char in puzzle_letters for char in word) and puzzle_letters[0] in word:
                sbg.add_word(word)

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

if __name__ == "__main__":
    spelling_bee()