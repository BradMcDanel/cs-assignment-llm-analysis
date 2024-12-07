from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

def load_dictionary(file_path):
    """Load the dictionary from a file and return it as a set for fast lookup."""
    with open(file_path, 'r') as file:
        return set(word.strip().lower() for word in file)

def is_valid_puzzle_input(puzzle):
    """Check if the user input for the puzzle is valid."""
    if len(puzzle) != 7:
        return False, "The puzzle must contain exactly seven characters."
    if not puzzle.isalpha():
        return False, "The puzzle must only contain alphabetic characters."
    if len(set(puzzle)) != 7:
        return False, "Each letter must be unique."
    return True, ""

def find_valid_words(dictionary, puzzle):
    """Find all valid words from the dictionary that can be formed with the puzzle."""
    center_letter = puzzle[0]
    valid_words = []
    for word in dictionary:
        if len(word) >= 4 and center_letter in word:
            if all(char in puzzle for char in word):
                valid_words.append(word)
    return valid_words

def calculate_word_score(word, puzzle):
    """Calculate the score of a word based on its length and if it's a pangram."""
    score = len(word) if len(word) > 4 else 1
    if all(char in word for char in puzzle):
        score += 7  # Pangram bonus
    return score

def spelling_bee():
    dictionary = load_dictionary(DICTIONARY_FILE)
    
    def puzzle_action(puzzle):
        valid, message = is_valid_puzzle_input(puzzle.upper())
        if valid:
            sbg.set_beehive_letters(puzzle.upper())
            sbg.show_message("")
        else:
            sbg.show_message(message, "Red")
    
    def solve_action(_):
        sbg.clear_word_list()
        puzzle = sbg.get_beehive_letters().lower()
        valid_words = find_valid_words(dictionary, puzzle)
        total_score = 0
        for word in valid_words:
            score = calculate_word_score(word, puzzle)
            total_score += score
            color = "Blue" if score > len(word) else "Black"
            sbg.add_word(f"{word} ({score})", color)
        sbg.show_message(f"Total words: {len(valid_words)}, Total score: {total_score}")

    # Setup the GUI
    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

# Startup code
if __name__ == "__main__":
    spelling_bee()