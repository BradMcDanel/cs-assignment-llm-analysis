from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

# Helper function to read dictionary
def read_dictionary():
    with open(DICTIONARY_FILE, 'r') as file:
        return set(word.strip().lower() for word in file.readlines())

# Helper function to check if a puzzle is legal
def is_legal_puzzle(puzzle):
    if len(puzzle) != 7:
        return False, "The puzzle must contain exactly seven characters."
    if not all(char.isalpha() for char in puzzle):
        return False, "Every character must be one of the 26 letters."
    if len(set(puzzle)) != 7:
        return False, "No letter may appear more than once in the puzzle."
    return True, ""

# Helper function to check if a word is valid for the puzzle
def is_valid_word(word, puzzle_letters, center_letter):
    if len(word) < 4:
        return False
    if center_letter not in word:
        return False
    if not all(char in puzzle_letters for char in word):
        return False
    return True

# Main function
def spelling_bee():
    dictionary = read_dictionary()

    def puzzle_action(s):
        legal, message = is_legal_puzzle(s)
        if legal:
            sbg.set_beehive_letters(s.upper())
            sbg.show_message("Puzzle set successfully.", "Green")
        else:
            sbg.show_message(message, "Red")

    def solve_action(s):
        puzzle_letters = sbg.get_beehive_letters().lower()
        center_letter = puzzle_letters[0]
        found_words = []
        total_score = 0
        for word in dictionary:
            if is_valid_word(word, puzzle_letters, center_letter):
                score = len(word) if len(word) > 4 else 1
                if len(set(word)) == 7:
                    score += 7  # Pangram bonus
                    sbg.add_word(word.upper(), "Blue")
                else:
                    sbg.add_word(word.upper())
                total_score += score
                found_words.append(word)
        message = f"Found {len(found_words)} words, Total score: {total_score}"
        sbg.show_message(message, "Green")

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

# Startup code
if __name__ == "__main__":
    spelling_bee()