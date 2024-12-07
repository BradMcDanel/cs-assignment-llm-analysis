# File: SpellingBee.py

from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

# Function to read the dictionary from the EnglishWords.txt data file into a list
def read_dictionary():
    with open(DICTIONARY_FILE, 'r') as file:
        return [word.strip().lower() for word in file]

# Function to check whether a word meets the requirements
def is_valid_word(word, puzzle):
    if len(word) < 4:
        return False
    if not all(letter in puzzle for letter in word):
        return False
    if puzzle[0] not in word:
        return False
    return True

# Function to check each word in the dictionary against the puzzle
def solve_puzzle(dictionary, puzzle, sbg):
    total_score = 0
    words_found = 0
    
    for word in dictionary:
        if is_valid_word(word, puzzle):
            words_found += 1
            score = len(word)
            if len(word) == 7:  # Pangram
                score += 7
                sbg.add_word(word, "Blue")
            else:
                sbg.add_word(word, "Black")
            total_score += score
    
    sbg.show_message(f"Words found: {words_found}, Total score: {total_score}")

def spelling_bee():
    def puzzle_action(puzzle):
        if len(puzzle) != 7 or not puzzle.isalpha() or len(set(puzzle)) != 7:
            sbg.show_message("Invalid puzzle. Puzzle must contain exactly 7 unique letters.", "Red")
        else:
            sbg.set_beehive_letters(puzzle.upper())
    
    def solve_action(s):
        dictionary = read_dictionary()
        puzzle = sbg.get_beehive_letters()
        solve_puzzle(dictionary, puzzle, sbg)

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

if __name__ == "__main__":
    spelling_bee()