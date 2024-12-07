from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

def load_dictionary(file_path):
    """Loads the dictionary from a text file."""
    with open(file_path, 'r') as file:
        return set(word.strip().lower() for word in file.readlines())

def is_legal_puzzle(puzzle):
    """Checks if the puzzle configuration is legal."""
    if len(puzzle) != 7:
        return False, "The puzzle must contain exactly seven characters."
    if not puzzle.isalpha():
        return False, "Every character must be a letter."
    if len(set(puzzle)) != 7:
        return False, "No letter may appear more than once."
    return True, ""

def find_legal_words(puzzle, dictionary):
    """Finds all legal words from the dictionary based on the puzzle rules."""
    center_letter = puzzle[0]
    legal_words = []
    for word in dictionary:
        if len(word) < 4:
            continue
        if center_letter not in word:
            continue
        if not all(c in puzzle for c in word):
            continue
        legal_words.append(word)
    return legal_words

def compute_score(word, puzzle):
    """Computes the score of a word."""
    score = len(word) if len(word) > 4 else 1
    if len(set(word)) == 7:
        score += 7  # Pangram bonus
    return score

def spelling_bee():
    """Main function for the Spelling Bee game."""
    sbg = SpellingBeeGraphics()
    dictionary = load_dictionary(DICTIONARY_FILE)

    def puzzle_action(s):
        legal, message = is_legal_puzzle(s.upper())
        if legal:
            sbg.set_beehive_letters(s.upper())
            sbg.show_message("Puzzle updated successfully.", "Green")
        else:
            sbg.show_message(message, "Red")

    def solve_action(s):
        sbg.clear_word_list()
        puzzle = sbg.get_beehive_letters().lower()
        legal_words = find_legal_words(puzzle, dictionary)
        total_score = 0
        for word in legal_words:
            score = compute_score(word, puzzle)
            color = "Blue" if len(set(word)) == 7 else "Black"
            sbg.add_word(f"{word} ({score})", color)
            total_score += score
        sbg.show_message(f"Total words: {len(legal_words)}, Total score: {total_score}", "Green")

    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

# Startup code
if __name__ == "__main__":
    spelling_bee()