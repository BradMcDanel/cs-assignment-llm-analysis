# Import necessary libraries
from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

# Function to read the dictionary from the file into a list
def read_dictionary():
    dictionary = []
    with open(DICTIONARY_FILE, "r") as file:
        for line in file:
            dictionary.append(line.strip())
    return dictionary

# Function to check if a word meets the puzzle requirements
def check_word(word, puzzle):
    # Check word length
    if len(word) < 4:
        return False
    # Check if word contains only puzzle letters
    for letter in word:
        if letter not in puzzle:
            return False
    # Check if word contains center letter
    if puzzle[0] not in word:
        return False
    return True

# Function to solve the Spelling Bee puzzle
def solve_puzzle(puzzle, dictionary):
    words_found = []
    total_score = 0
    pangram_found = False

    for word in dictionary:
        if check_word(word, puzzle):
            words_found.append(word)
            # Calculate word score
            score = len(word)
            if len(word) == 7:
                score += 7  # Pangram bonus
                pangram_found = True
            total_score += score

    return words_found, total_score, pangram_found

def puzzle_action(s):
    puzzle = sbg.get_field("Puzzle")
    if len(puzzle) != 7 or not puzzle.isalpha() or len(set(puzzle)) != 7:
        sbg.show_message("Invalid puzzle input. Please enter exactly 7 unique letters.", "Red")
    else:
        sbg.set_beehive_letters(puzzle.upper())

def solve_action(s):
    puzzle = sbg.get_beehive_letters()
    dictionary = read_dictionary()
    words_found, total_score, pangram_found = solve_puzzle(puzzle, dictionary)
    
    sbg.clear_word_list()
    for word in words_found:
        color = "Blue" if len(word) == 7 else "Black"
        sbg.add_word(word, color)
    
    message = f"Total words found: {len(words_found)}, Total score: {total_score}"
    sbg.show_message(message, "Green")

# Startup code
def spelling_bee():
    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

if __name__ == "__main__":
    spelling_bee()