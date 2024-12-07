from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

# Utility function to read dictionary file
def read_dictionary_file(file_name):
    with open(file_name, 'r') as file:
        return [word.strip().lower() for word in file]

# Check if a word meets the requirements
def is_valid_word(word, puzzle_letters):
    if len(word) < 4:
        return False
    if not all(char in puzzle_letters for char in word):
        return False
    if puzzle_letters[0] not in word:
        return False
    return True

# Function to solve Spelling Bee puzzle
def solve_puzzle(puzzle_letters, dictionary):
    words_found = []
    total_score = 0

    for word in dictionary:
        if is_valid_word(word, puzzle_letters):
            words_found.append(word)
            word_score = len(word) if len(word) >= 4 else 1
            if len(set(word)) == 7:
                word_score += 7
            total_score += word_score

    return words_found, total_score

# Main program
def spelling_bee():
    def puzzle_action(s):
        puzzle = sbg.get_field("Puzzle").upper()
        if len(puzzle) != 7 or not all(char.isalpha() for char in puzzle) or len(set(puzzle)) != 7:
            sbg.show_message("Invalid puzzle. Please enter exactly seven unique letters.", "Red")
        else:
            sbg.set_beehive_letters(puzzle)

    def solve_action(s):
        puzzle_letters = sbg.get_beehive_letters()
        dictionary = read_dictionary_file(DICTIONARY_FILE)
        words_found, total_score = solve_puzzle(puzzle_letters, dictionary)
        
        sbg.clear_word_list()
        for word in words_found:
            color = "Blue" if len(set(word)) == 7 else "Black"
            sbg.add_word(word, color)
        
        sbg.show_message(f"Found {len(words_found)} words. Total score: {total_score}", "Black")

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

# Startup code
if __name__ == "__main__":
    spelling_bee()