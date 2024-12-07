# Your code for Milestone 2: Display the legal words in the SpellingBee puzzle

from SpellingBeeGraphics import SpellingBeeGraphics

def solve_action(s):
    puzzle = sbg.get_beehive_letters()
    words = read_dictionary(DICTIONARY_FILE)
    
    for word in words:
        if is_legal_word(word, puzzle):
            sbg.add_word(word)
            
def read_dictionary(file):
    with open(file, 'r') as f:
        return [word.strip() for word in f]

def is_legal_word(word, puzzle):
    if len(word) < 4:
        return False
    if set(word) - set(puzzle):
        return False
    if puzzle[0] not in word:
        return False
    return True

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

# Startup code
sbg = SpellingBeeGraphics()
sbg.add_field("Puzzle", puzzle_action)
sbg.add_button("Solve", solve_action)