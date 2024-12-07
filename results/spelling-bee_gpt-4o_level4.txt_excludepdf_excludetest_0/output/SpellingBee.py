from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

# Helper function to read the dictionary file
def read_dictionary(file_path):
    with open(file_path, "r") as file:
        return set(word.strip().lower() for word in file)

# Helper function to check if a puzzle is legal
def is_legal_puzzle(puzzle):
    if len(puzzle) != 7:
        return "The puzzle must contain exactly seven characters."
    if not puzzle.isalpha() or not puzzle.islower():
        return "Every character must be a lowercase letter."
    if len(set(puzzle)) != 7:
        return "No letter may appear more than once in the puzzle."
    return None

# Helper function to check if a word is valid
def is_valid_word(word, beehive_letters, center_letter):
    return (len(word) >= 4 and
            set(word).issubset(beehive_letters) and
            center_letter in word)

# Main function to handle the Spelling Bee game logic
def spelling_bee():
    dictionary = read_dictionary(DICTIONARY_FILE)

    def puzzle_action(puzzle):
        error_message = is_legal_puzzle(puzzle)
        if error_message:
            sbg.show_message(error_message, "Red")
        else:
            sbg.set_beehive_letters(puzzle.upper())
            sbg.show_message("Puzzle set successfully!", "Green")

    def solve_action(_):
        puzzle = sbg.get_beehive_letters().lower()
        if not puzzle or not is_legal_puzzle(puzzle):
            sbg.show_message("Please enter a valid puzzle first.", "Red")
            return

        center_letter = puzzle[0]
        words_found = 0
        total_score = 0
        sbg.clear_word_list()

        for word in dictionary:
            if is_valid_word(word, set(puzzle), center_letter):
                score = len(word)
                is_pangram = len(set(word)) == 7
                if is_pangram:
                    score += 7
                    sbg.add_word(word, "Blue")
                else:
                    sbg.add_word(word, "Black")
                total_score += score
                words_found += 1

        sbg.show_message(f"Found {words_found} words with a total score of {total_score}.", "Green")

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

# Startup code
if __name__ == "__main__":
    spelling_bee()