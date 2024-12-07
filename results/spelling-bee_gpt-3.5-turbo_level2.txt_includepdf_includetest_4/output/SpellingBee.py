# File: SpellingBee.py

from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

# Starter program
def spelling_bee():
    def puzzle_action(s):
        puzzle_letters = sbg.get_field("Puzzle").upper()
        if len(puzzle_letters) != 7 or not puzzle_letters.isalpha() or len(set(puzzle_letters)) != 7:
            sbg.show_message("Invalid puzzle format. Please enter exactly 7 unique alphabetic characters.", "Red")
        else:
            sbg.set_beehive_letters(puzzle_letters)

    def solve_action(s):
        sbg.clear_word_list()
        puzzle_letters = sbg.get_beehive_letters()
        # Read dictionary words
        with open(DICTIONARY_FILE, 'r') as file:
            dictionary_words = [word.strip().lower() for word in file.readlines()]

        for word in dictionary_words:
            if len(word) >= 4 and all(char in puzzle_letters for char in word) and puzzle_letters[0] in word:
                if len(word) == 7:
                    sbg.add_word(word, "Blue")  # Pangram
                else:
                    sbg.add_word(word)
                    
# Startup code
if __name__ == "__main__":
    spelling_bee()