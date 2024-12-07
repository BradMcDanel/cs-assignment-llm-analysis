from SpellingBeeGraphics import SpellingBeeGraphics
from utils import load_dictionary, is_valid_puzzle, find_words

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

# Starter program
def spelling_bee():
    # Load the dictionary
    dictionary = load_dictionary(DICTIONARY_FILE)

    def puzzle_action(puzzle_string):
        # Validate the puzzle input
        validation_message = is_valid_puzzle(puzzle_string)
        if validation_message:
            sbg.show_message(validation_message, "Red")
            return

        # Set the beehive letters
        sbg.set_beehive_letters(puzzle_string.upper())
        sbg.clear_word_list()
        sbg.show_message("Puzzle set successfully. You can now try to solve it!", "Green")

    def solve_action(_):
        # Get the current beehive letters
        puzzle_string = sbg.get_beehive_letters().lower()
        center_letter = puzzle_string[0]

        # Find valid words
        words = find_words(dictionary, puzzle_string, center_letter)
        
        # Display words and calculate score
        total_score, word_count = 0, 0
        for word, score, is_pangram in words:
            color = "Blue" if is_pangram else "Black"
            sbg.add_word(f"{word} ({score})", color)
            total_score += score
            word_count += 1

        # Show final results
        sbg.show_message(f"Found {word_count} words with a total score of {total_score}.", "Green")

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

# Startup code
if __name__ == "__main__":
    spelling_bee()