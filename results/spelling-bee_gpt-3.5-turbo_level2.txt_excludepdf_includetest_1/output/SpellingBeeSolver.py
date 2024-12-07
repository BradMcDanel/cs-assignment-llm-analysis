from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

# Load dictionary words into a list
def load_dictionary():
    with open(DICTIONARY_FILE, 'r') as file:
        dictionary = [word.strip().lower() for word in file]
    return dictionary

# Check if a word is valid based on puzzle rules
def is_valid_word(word, puzzle):
    center_letter = puzzle[0]
    if len(word) < 4 or center_letter not in word:
        return False
    for char in word:
        if char not in puzzle:
            return False
    return True

# Solve the Spelling Bee puzzle
def solve_puzzle(puzzle, dictionary, sbg):
    word_list = []
    total_score = 0
    pangram_found = False

    for word in dictionary:
        if is_valid_word(word, puzzle):
            word_list.append(word)
            score = len(word)
            if len(word) == 7:  # Pangram
                score += 7
                pangram_found = True
            total_score += score
            sbg.add_word(word, "Black" if len(word) < 7 else "Blue")

    sbg.show_message(f"Total words found: {len(word_list)} | Total score: {total_score}", "Black")
    if pangram_found:
        sbg.show_message("Pangram found!", "Blue")

def puzzle_action(puzzle):
    if len(puzzle) != 7 or not puzzle.isalpha() or len(set(puzzle)) != 7:
        sbg.show_message("Invalid puzzle. Please enter exactly 7 unique letters.", "Red")
    else:
        sbg.set_beehive_letters(puzzle.upper())

def solve_action(button_name):
    puzzle = sbg.get_beehive_letters()
    dictionary = load_dictionary()
    solve_puzzle(puzzle, dictionary, sbg)

def spelling_bee():
    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

if __name__ == "__main__":
    spelling_bee()