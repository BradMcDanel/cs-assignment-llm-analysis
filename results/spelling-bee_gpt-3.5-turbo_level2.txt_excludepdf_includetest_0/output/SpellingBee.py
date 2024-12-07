from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

# Read dictionary file into a list
def read_dictionary():
    with open(DICTIONARY_FILE, 'r') as file:
        dictionary = [word.strip().lower() for word in file]
    return dictionary

# Check if a word meets the requirements
def is_valid_word(word, puzzle_letters):
    center_letter = puzzle_letters[0]
    if len(word) < 4 or center_letter not in word:
        return False
    for letter in word:
        if letter not in puzzle_letters:
            return False
    return True

# Check words in the dictionary against the puzzle
def check_words_in_puzzle(dictionary, puzzle_letters, sbg):
    words_found = []
    total_score = 0
    pangram_found = False

    for word in dictionary:
        if is_valid_word(word, puzzle_letters):
            words_found.append(word)
            score = len(word)
            if len(word) == 7:
                score += 7  # Pangram bonus
                pangram_found = True
            total_score += score
            sbg.add_word(word, "Blue" if len(word) == 7 else "Black")

    sbg.show_message(f"Found {len(words_found)} words with a total score of {total_score}", "Black")
    if pangram_found:
        sbg.show_message("Pangram found!", "Black")

# Main function for Spelling Bee
def spelling_bee():
    def puzzle_action(s):
        puzzle = sbg.get_field("Puzzle")
        if len(puzzle) != 7 or not puzzle.isalpha() or len(set(puzzle)) != 7:
            sbg.show_message("Invalid puzzle, must contain exactly 7 unique letters", "Red")
        else:
            sbg.set_beehive_letters(puzzle.upper())

    def solve_action(s):
        puzzle_letters = sbg.get_beehive_letters()
        dictionary = read_dictionary()
        check_words_in_puzzle(dictionary, puzzle_letters, sbg)

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

# Startup code
if __name__ == "__main__":
    spelling_bee()