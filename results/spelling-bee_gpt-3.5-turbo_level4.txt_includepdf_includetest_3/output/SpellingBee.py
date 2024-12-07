from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

# Starter program
def spelling_bee():
    def puzzle_action(s):
        puzzle = sbg.get_field("Puzzle")
        if len(puzzle) != 7:
            sbg.show_message("Puzzle must contain exactly 7 characters.", "Red")
        elif not puzzle.isalpha() or len(set(puzzle)) != 7:
            sbg.show_message("Puzzle must contain unique alphabetic characters.", "Red")
        else:
            sbg.set_beehive_letters(puzzle)

    def solve_action(s):
        sbg.clear_word_list()
        puzzle = sbg.get_beehive_letters()
        with open(DICTIONARY_FILE, 'r') as file:
            for line in file:
                word = line.strip()
                if len(word) >= 4 and all(char in puzzle for char in word) and puzzle[0] in word:
                    sbg.add_word(word)
    
    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

# Startup code
if __name__ == "__main__":
    spelling_bee()