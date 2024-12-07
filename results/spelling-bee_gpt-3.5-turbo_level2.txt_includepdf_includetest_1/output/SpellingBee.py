# File: SpellingBee.py

from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

# Load English words from dictionary file into a list
def load_dictionary(file):
    with open(file, 'r') as f:
        words = [line.strip() for line in f]
    return words

# Check if a word meets the requirements for the puzzle
def check_word(word, puzzle):
    if len(word) < 4:
        return False
    if any(char not in puzzle for char in word):
        return False
    if puzzle[0] not in word:
        return False
    return True

# Solve the Spelling Bee puzzle
def solve_puzzle(puzzle, dictionary):
    legal_words = [word for word in dictionary if check_word(word, puzzle)]
    return legal_words

def spelling_bee():
    def puzzle_action(s):
        letters = sbg.get_field("Puzzle").upper()
        if len(letters) != 7 or not letters.isalpha() or len(set(letters)) != 7:
            sbg.show_message("Invalid puzzle. Must contain exactly 7 unique letters.", "Red")
        else:
            sbg.set_beehive_letters(letters)

    def solve_action(s):
        puzzle = sbg.get_beehive_letters()
        dictionary = load_dictionary(DICTIONARY_FILE)
        legal_words = solve_puzzle(puzzle, dictionary)
        sbg.clear_word_list()
        score = 0
        pangram_found = False
        for word in legal_words:
            if len(word) == 7:
                pangram_found = True
                sbg.add_word(word, "Blue")
                score += 7
            else:
                sbg.add_word(word)
                score += len(word)
        sbg.show_message(f"Found {len(legal_words)} words. Total score: {score}.", "Black")
        if pangram_found:
            sbg.show_message("Pangram found!", "Blue")

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

# Startup code
if __name__ == "__main__":
    spelling_bee()