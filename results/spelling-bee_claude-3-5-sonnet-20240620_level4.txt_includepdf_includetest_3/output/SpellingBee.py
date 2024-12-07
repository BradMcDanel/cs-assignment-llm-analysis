# File: SpellingBee.py

"""
This file implements the SpellingBee game.
"""

from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

def spelling_bee():
    # Load the dictionary
    dictionary = load_dictionary(DICTIONARY_FILE)
    
    # Initialize the graphics
    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)
    sbg.add_field("Word", word_action)

    # Global variables
    global puzzle_letters, found_words, total_score

    puzzle_letters = ""
    found_words = set()
    total_score = 0

    def puzzle_action(s):
        global puzzle_letters
        if is_valid_puzzle(s):
            puzzle_letters = s.upper()
            sbg.set_beehive_letters(puzzle_letters)
            sbg.show_message("Puzzle set successfully!")
            sbg.clear_word_list()
            found_words.clear()
            update_score_display()
        else:
            sbg.show_message("Invalid puzzle. Please enter 7 unique letters.", "Red")

    def solve_action(s):
        if not puzzle_letters:
            sbg.show_message("Please set a puzzle first.", "Red")
            return
        
        sbg.clear_word_list()
        found_words.clear()
        
        for word in dictionary:
            if is_valid_word(word):
                add_word(word)
        
        update_score_display()

    def word_action(s):
        word = s.lower()
        if not puzzle_letters:
            sbg.show_message("Please set a puzzle first.", "Red")
        elif word in found_words:
            sbg.show_message(f"'{word}' has already been found.", "Red")
        elif is_valid_word(word):
            add_word(word)
            update_score_display()
            sbg.set_field("Word", "")
        else:
            sbg.show_message(f"'{word}' is not a valid word for this puzzle.", "Red")

    def is_valid_puzzle(s):
        return (len(s) == 7 and
                s.isalpha() and
                len(set(s.upper())) == 7)

    def is_valid_word(word):
        return (len(word) >= 4 and
                set(word).issubset(set(puzzle_letters.lower())) and
                puzzle_letters[0].lower() in word and
                word in dictionary)

    def add_word(word):
        score = calculate_score(word)
        color = "Blue" if set(word) == set(puzzle_letters.lower()) else "Black"
        sbg.add_word(f"{word} ({score})", color)
        found_words.add(word)

    def calculate_score(word):
        base_score = len(word) if len(word) > 4 else 1
        pangram_bonus = 7 if set(word) == set(puzzle_letters.lower()) else 0
        return base_score + pangram_bonus

    def update_score_display():
        global total_score
        total_score = sum(calculate_score(word) for word in found_words)
        sbg.show_message(f"Words: {len(found_words)}, Score: {total_score}")

def load_dictionary(filename):
    with open(filename, 'r') as f:
        return set(word.strip().lower() for word in f)

# Startup code
if __name__ == "__main__":
    spelling_bee()