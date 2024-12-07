from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

def read_dictionary(file_path):
    """Reads the dictionary file and returns a set of words."""
    with open(file_path, 'r') as file:
        return set(word.strip().lower() for word in file)

def is_legal_puzzle(puzzle):
    """Checks if the given puzzle is legal."""
    if len(puzzle) != 7:
        return False, "Puzzle must contain exactly seven letters."
    if not puzzle.isalpha():
        return False, "Puzzle must contain only alphabetic characters."
    if len(set(puzzle)) != 7:
        return False, "No letter may appear more than once in the puzzle."
    return True, ""

def find_legal_words(puzzle, dictionary):
    """Finds all legal words from the dictionary that satisfy the puzzle rules."""
    center_letter = puzzle[0].lower()
    valid_letters = set(puzzle.lower())

    def is_valid_word(word):
        if len(word) < 4:
            return False
        if center_letter not in word:
            return False
        if not set(word).issubset(valid_letters):
            return False
        return True

    return [word for word in dictionary if is_valid_word(word)]

def calculate_score(word, is_pangram):
    """Calculate the score for a given word."""
    base_score = len(word) if len(word) > 4 else 1
    return base_score + (7 if is_pangram else 0)

def spelling_bee():
    dictionary = read_dictionary(DICTIONARY_FILE)

    def puzzle_action(puzzle):
        is_legal, message = is_legal_puzzle(puzzle)
        if not is_legal:
            sbg.show_message(message, "Red")
        else:
            sbg.set_beehive_letters(puzzle)
            sbg.show_message("Puzzle set successfully", "Green")

    def solve_action(_):
        sbg.clear_word_list()
        puzzle = sbg.get_beehive_letters().lower()
        legal_words = find_legal_words(puzzle, dictionary)
        total_score, word_count = 0, 0
        for word in legal_words:
            is_pangram = len(set(word)) == 7
            score = calculate_score(word, is_pangram)
            color = "Blue" if is_pangram else "Black"
            sbg.add_word(f"{word.upper()} ({score})", color)
            total_score += score
            word_count += 1
        sbg.show_message(f"{word_count} words, {total_score} points", "Black")

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

# Startup code
if __name__ == "__main__":
    spelling_bee()