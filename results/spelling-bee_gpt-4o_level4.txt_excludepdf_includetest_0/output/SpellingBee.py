from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

def load_dictionary():
    """Loads the dictionary file into a set for quick lookup."""
    with open(DICTIONARY_FILE, 'r') as file:
        return set(word.strip().lower() for word in file)

def is_legal_puzzle(puzzle):
    """Checks if the given puzzle string is legal."""
    if len(puzzle) != 7:
        return "The puzzle must contain exactly seven characters."
    if not puzzle.isalpha():
        return "Every character must be a letter."
    if len(set(puzzle)) != 7:
        return "No letter may appear more than once."
    return None

def find_legal_words(puzzle, dictionary):
    """Finds all legal words that can be formed with the given puzzle."""
    center_letter = puzzle[0]
    legal_words = []

    for word in dictionary:
        if len(word) >= 4 and center_letter in word and all(char in puzzle for char in word):
            legal_words.append(word)
    
    return legal_words

def calculate_word_score(word, is_pangram):
    """Calculates the score for a given word."""
    score = len(word)
    if is_pangram:
        score += 7
    return score

def spelling_bee():
    dictionary = load_dictionary()

    def puzzle_action(puzzle):
        puzzle = puzzle.upper()
        error_message = is_legal_puzzle(puzzle)
        if error_message:
            sbg.show_message(error_message, "Red")
        else:
            sbg.set_beehive_letters(puzzle)

    def solve_action(_):
        sbg.clear_word_list()
        puzzle = sbg.get_beehive_letters().lower()
        legal_words = find_legal_words(puzzle, dictionary)
        total_score = 0
        total_words = len(legal_words)

        for word in legal_words:
            is_pangram = set(word) == set(puzzle)
            score = calculate_word_score(word, is_pangram)
            total_score += score
            color = "Blue" if is_pangram else "Black"
            sbg.add_word(f"{word} ({score})", color)

        sbg.show_message(f"Total Words: {total_words}, Total Score: {total_score}")

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

# Startup code
if __name__ == "__main__":
    spelling_bee()