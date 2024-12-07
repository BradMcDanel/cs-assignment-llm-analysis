from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

# Load dictionary words from file into a list
def load_dictionary():
    with open(DICTIONARY_FILE, 'r') as file:
        return [word.strip() for word in file]

# Check if a word is valid based on the puzzle rules
def is_valid_word(word, puzzle_letters):
    if len(word) < 4 or len(set(word) - set(puzzle_letters)) > 0 or puzzle_letters[0] not in word:
        return False
    return True

# Milestone #1: Initialize the beehive with the letters in the puzzle field
def puzzle_action(s):
    letters = sbg.get_field("Puzzle")
    if len(letters) == 7 and letters.isalpha() and len(set(letters)) == 7:
        sbg.set_beehive_letters(letters.upper())
    else:
        sbg.show_message("Invalid puzzle. Please enter exactly 7 unique alphabetic characters.", "Red")

# Milestone #2: Display the legal words in the SpellingBee puzzle
def solve_action(s):
    puzzle_letters = sbg.get_beehive_letters()
    dictionary = load_dictionary()
    sbg.clear_word_list()
    total_score = 0
    words_found = 0

    for word in dictionary:
        if is_valid_word(word, puzzle_letters):
            sbg.add_word(word, "Black")
            words_found += 1
            word_score = len(word) if len(word) < 7 else len(word) + 7
            total_score += word_score

    sbg.show_message(f"Words found: {words_found}. Total score: {total_score}", "Black")

def spelling_bee():
    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

if __name__ == "__main__":
    spelling_bee()