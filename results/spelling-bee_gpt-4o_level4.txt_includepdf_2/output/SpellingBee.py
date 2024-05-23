# File: SpellingBee.py

"""
This file is the starter file for the SpellingBee project.
"""

from SpellingBeeGraphics import SpellingBeeGraphics
import string

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

# Helper function to read dictionary
def read_dictionary():
    with open(DICTIONARY_FILE) as file:
        return set(word.strip().lower() for word in file)

# Check if the puzzle string is a valid puzzle
def is_valid_puzzle(puzzle):
    if len(puzzle) != 7:
        return "The puzzle must contain exactly seven characters."
    if any(char not in string.ascii_letters for char in puzzle):
        return "The puzzle must only contain letters."
    if len(set(puzzle)) != 7:
        return "The puzzle must not contain duplicate letters."
    return None

# Check if a word is valid within the given puzzle
def is_valid_word(word, letters, center_letter):
    return (
        len(word) >= 4 and 
        center_letter in word and 
        all(char in letters for char in word)
    )

# Calculate score for a word
def calculate_score(word):
    if len(set(word)) == 7:
        return len(word) + 7  # Pangram bonus
    return len(word) if len(word) > 4 else 1

# Starter program
def spelling_bee():
    dictionary = read_dictionary()
    found_words = set()
    sbg = SpellingBeeGraphics()

    def puzzle_action(puzzle):
        puzzle = puzzle.upper()
        validation_error = is_valid_puzzle(puzzle)
        if validation_error:
            sbg.show_message(validation_error, "Red")
        else:
            sbg.set_beehive_letters(puzzle)
            sbg.show_message("")

    def solve_action(button_name):
        sbg.clear_word_list()
        puzzle = sbg.get_beehive_letters()
        center_letter = puzzle[0]
        words = [
            word for word in dictionary 
            if is_valid_word(word, puzzle, center_letter)
        ]
        total_score = 0
        for word in words:
            if len(set(word)) == 7:
                sbg.add_word(f"{word} ({calculate_score(word)})", "Blue")
            else:
                sbg.add_word(f"{word} ({calculate_score(word)})")
            total_score += calculate_score(word)
        sbg.show_message(f"Found {len(words)} words with a total score of {total_score}")

    def word_action(word):
        word = word.lower()
        puzzle = sbg.get_beehive_letters().lower()
        center_letter = puzzle[0]
        if word in found_words:
            sbg.show_message(f"'{word}' has already been found.", "Red")
        elif word not in dictionary:
            sbg.show_message(f"'{word}' is not in the dictionary.", "Red")
        elif not is_valid_word(word, puzzle, center_letter):
            sbg.show_message(f"'{word}' is not a valid word.", "Red")
        else:
            found_words.add(word)
            sbg.add_word(f"{word} ({calculate_score(word)})")
            sbg.show_message("")
            sbg.set_field("Word", "")

    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)
    sbg.add_field("Word", word_action)

# Startup code
if __name__ == "__main__":
    spelling_bee()