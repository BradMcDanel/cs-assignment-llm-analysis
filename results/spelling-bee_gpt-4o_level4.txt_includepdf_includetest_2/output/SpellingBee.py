# File: SpellingBee.py

"""
This file is the solution file for the SpellingBee project.
"""

from SpellingBeeGraphics import SpellingBeeGraphics

# Constants

DICTIONARY_FILE = "EnglishWords.txt"

def read_dictionary():
    """Reads the dictionary file into a set of words."""
    with open(DICTIONARY_FILE, 'r') as f:
        return set(word.strip() for word in f)

def is_legal_puzzle(puzzle):
    """Checks if a puzzle is legal based on the given criteria."""
    if len(puzzle) != 7:
        return False, "The puzzle must contain exactly seven characters."
    if not puzzle.isalpha():
        return False, "Every character must be a letter."
    if len(set(puzzle)) != 7:
        return False, "No letter may appear more than once in the puzzle."
    return True, ""

def spelling_bee():
    dictionary = read_dictionary()

    def puzzle_action(puzzle):
        puzzle = puzzle.upper()
        is_legal, message = is_legal_puzzle(puzzle)
        if is_legal:
            sbg.set_beehive_letters(puzzle)
            sbg.show_message("Puzzle initialized.", "Green")
        else:
            sbg.show_message(message, "Red")

    def solve_action(s):
        beehive_letters = sbg.get_beehive_letters().lower()
        center_letter = beehive_letters[0]
        legal_words = []
        total_score = 0
        pangrams = []

        sbg.clear_word_list()

        for word in dictionary:
            if len(word) >= 4 and center_letter in word and all(c in beehive_letters for c in word):
                score = len(word) if len(word) > 4 else 1
                if set(word) == set(beehive_letters):
                    score += 7
                    pangrams.append(word)
                legal_words.append((word, score))
                total_score += score

        for word, score in legal_words:
            color = "Blue" if word in pangrams else "Black"
            sbg.add_word(f"{word} ({score})", color)

        sbg.show_message(f"Total words: {len(legal_words)}, Total score: {total_score}", "Black")

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

# Startup code

if __name__ == "__main__":
    spelling_bee()