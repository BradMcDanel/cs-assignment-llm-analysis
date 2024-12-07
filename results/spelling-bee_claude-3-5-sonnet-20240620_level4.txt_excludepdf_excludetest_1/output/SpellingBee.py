# File: SpellingBee.py

"""
This program implements the Spelling Bee game from the New York Times.
It allows users to enter a puzzle, solve it automatically, and play interactively.
"""

from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

def spelling_bee():
    sbg = SpellingBeeGraphics()
    words = read_dictionary(DICTIONARY_FILE)
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
        nonlocal found_words, total_score
        if not puzzle_letters:
            sbg.show_message("Please set a puzzle first.", "Red")
            return
        
        sbg.clear_word_list()
        found_words.clear()
        total_score = 0
        
        for word in words:
            if is_valid_word(word, puzzle_letters):
                add_word(word)
        
        update_score_display()

    def word_action(s):
        word = s.lower()
        if not puzzle_letters:
            sbg.show_message("Please set a puzzle first.", "Red")
        elif word in found_words:
            sbg.show_message("Word already found!", "Red")
        elif not is_valid_word(word, puzzle_letters):
            sbg.show_message(get_invalid_reason(word, puzzle_letters), "Red")
        else:
            add_word(word)
            update_score_display()
        sbg.set_field("Word", "")

    def add_word(word):
        nonlocal found_words, total_score
        found_words.add(word)
        score = calculate_word_score(word, puzzle_letters)
        total_score += score
        color = "Blue" if is_pangram(word, puzzle_letters) else "Black"
        sbg.add_word(f"{word} ({score})", color)

    def update_score_display():
        msg = f"Words: {len(found_words)}, Score: {total_score}"
        sbg.show_message(msg, "Green")

    sbg.add_field("Puzzle", puzzle_action, 7)
    sbg.add_field("Word", word_action, 15)
    sbg.add_button("Solve", solve_action)

def read_dictionary(filename):
    with open(filename, "r") as file:
        return set(word.strip().lower() for word in file)

def is_valid_puzzle(puzzle):
    return (len(puzzle) == 7 and
            puzzle.isalpha() and
            len(set(puzzle.lower())) == 7)

def is_valid_word(word, puzzle):
    center = puzzle[0].lower()
    puzzle_set = set(puzzle.lower())
    return (len(word) >= 4 and
            center in word and
            all(letter in puzzle_set for letter in word))

def get_invalid_reason(word, puzzle):
    if len(word) < 4:
        return "Word must be at least 4 letters long."
    if puzzle[0].lower() not in word:
        return "Word must contain the center letter."
    invalid_letters = set(word) - set(puzzle.lower())
    if invalid_letters:
        return f"Word contains invalid letters: {', '.join(invalid_letters)}"
    return "Word is not in the dictionary."

def calculate_word_score(word, puzzle):
    score = len(word) if len(word) > 4 else 1
    if is_pangram(word, puzzle):
        score += 7
    return score

def is_pangram(word, puzzle):
    return set(word) == set(puzzle.lower())

# Startup code
if __name__ == "__main__":
    spelling_bee()