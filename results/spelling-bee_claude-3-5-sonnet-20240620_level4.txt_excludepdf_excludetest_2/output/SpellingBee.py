# File: SpellingBee.py

"""
This file implements the Spelling Bee game as described in the project instructions.
It includes functionality for initializing the beehive, solving the puzzle,
adding scores, and allowing user interaction.
"""

from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"
MIN_WORD_LENGTH = 4

def spelling_bee():
    sbg = SpellingBeeGraphics()
    dictionary = load_dictionary(DICTIONARY_FILE)
    puzzle_letters = ""
    found_words = set()
    total_score = 0

    def puzzle_action(s):
        nonlocal puzzle_letters
        if is_valid_puzzle(s):
            puzzle_letters = s.upper()
            sbg.set_beehive_letters(puzzle_letters)
            sbg.show_message("Puzzle set successfully!", "Green")
        else:
            sbg.show_message("Invalid puzzle. Please enter 7 unique letters.", "Red")

    def solve_action(s):
        if not puzzle_letters:
            sbg.show_message("Please set a valid puzzle first.", "Red")
            return
        
        sbg.clear_word_list()
        words = find_valid_words(dictionary, puzzle_letters)
        display_words(words)
        show_summary(len(words), calculate_total_score(words))

    def word_action(s):
        nonlocal found_words, total_score
        word = s.lower()
        if not puzzle_letters:
            sbg.show_message("Please set a valid puzzle first.", "Red")
        elif word in found_words:
            sbg.show_message(f"You've already found '{word}'!", "Orange")
        elif is_valid_word(word, puzzle_letters, dictionary):
            score = calculate_word_score(word, puzzle_letters)
            found_words.add(word)
            total_score += score
            sbg.add_word(f"{word} ({score})", "Blue" if is_pangram(word, puzzle_letters) else "Black")
            sbg.set_field("Word", "")
            show_summary(len(found_words), total_score)
        else:
            sbg.show_message(get_invalid_word_message(word, puzzle_letters), "Red")

    sbg.add_field("Puzzle", puzzle_action, 7)
    sbg.add_field("Word", word_action, 15)
    sbg.add_button("Solve", solve_action)

def load_dictionary(filename):
    with open(filename, 'r') as file:
        return set(word.strip().lower() for word in file)

def is_valid_puzzle(s):
    return len(s) == 7 and s.isalpha() and len(set(s)) == 7

def find_valid_words(dictionary, puzzle_letters):
    center_letter = puzzle_letters[0].lower()
    valid_letters = set(puzzle_letters.lower())
    return [word for word in dictionary if is_valid_word(word, puzzle_letters, dictionary)]

def is_valid_word(word, puzzle_letters, dictionary):
    if len(word) < MIN_WORD_LENGTH or word not in dictionary:
        return False
    if puzzle_letters[0].lower() not in word:
        return False
    return all(letter in puzzle_letters.lower() for letter in word)

def calculate_word_score(word, puzzle_letters):
    base_score = max(1, len(word))
    return base_score + (7 if is_pangram(word, puzzle_letters) else 0)

def is_pangram(word, puzzle_letters):
    return set(word) == set(puzzle_letters.lower())

def calculate_total_score(words):
    return sum(calculate_word_score(word, set(word)) for word in words)

def display_words(words):
    for word in sorted(words):
        score = calculate_word_score(word, set(word))
        color = "Blue" if is_pangram(word, set(word)) else "Black"
        sbg.add_word(f"{word} ({score})", color)

def show_summary(word_count, total_score):
    sbg.show_message(f"Found {word_count} words. Total score: {total_score}", "Green")

def get_invalid_word_message(word, puzzle_letters):
    if len(word) < MIN_WORD_LENGTH:
        return f"'{word}' is too short. Words must be at least {MIN_WORD_LENGTH} letters long."
    if puzzle_letters[0].lower() not in word:
        return f"'{word}' doesn't contain the center letter '{puzzle_letters[0]}'."
    if not all(letter in puzzle_letters.lower() for letter in word):
        return f"'{word}' contains letters not in the puzzle."
    return f"'{word}' is not in the dictionary."

# Startup code
if __name__ == "__main__":
    spelling_bee()