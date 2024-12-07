# File: SpellingBee.py

"""
This file implements the Spelling Bee game.
"""

from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

def spelling_bee():
    def read_dictionary():
        with open(DICTIONARY_FILE, 'r') as file:
            return set(word.strip().lower() for word in file)

    def is_valid_puzzle(puzzle):
        return (len(puzzle) == 7 and
                puzzle.isalpha() and
                len(set(puzzle)) == 7)

    def is_valid_word(word, puzzle):
        center = puzzle[0].lower()
        puzzle_set = set(puzzle.lower())
        return (len(word) >= 4 and
                set(word).issubset(puzzle_set) and
                center in word)

    def calculate_score(word, puzzle):
        score = len(word)
        if score == 4:
            score = 1
        if set(word) == set(puzzle.lower()):
            score += 7
        return score

    def update_score_message(words, total_score):
        sbg.show_message(f"Words: {len(words)}, Score: {total_score}")

    def puzzle_action(s):
        puzzle = s.upper()
        if is_valid_puzzle(puzzle):
            sbg.set_beehive_letters(puzzle)
            sbg.show_message("")
        else:
            sbg.show_message("Invalid puzzle. Please enter 7 unique letters.", "Red")

    def solve_action(s):
        puzzle = sbg.get_beehive_letters()
        if not puzzle:
            sbg.show_message("Please enter a valid puzzle first.", "Red")
            return

        sbg.clear_word_list()
        words = []
        total_score = 0

        for word in dictionary:
            if is_valid_word(word, puzzle):
                score = calculate_score(word, puzzle)
                color = "Blue" if len(set(word)) == 7 else "Black"
                sbg.add_word(f"{word} ({score})", color)
                words.append(word)
                total_score += score

        update_score_message(words, total_score)

    def word_action(s):
        puzzle = sbg.get_beehive_letters()
        if not puzzle:
            sbg.show_message("Please enter a valid puzzle first.", "Red")
            return

        word = s.lower()
        if word not in dictionary:
            sbg.show_message("Word not in dictionary.", "Red")
        elif not is_valid_word(word, puzzle):
            if len(word) < 4:
                sbg.show_message("Word must be at least 4 letters long.", "Red")
            elif puzzle[0].lower() not in word:
                sbg.show_message("Word must contain the center letter.", "Red")
            else:
                sbg.show_message("Word contains invalid letters.", "Red")
        elif word in found_words:
            sbg.show_message("Word already found.", "Red")
        else:
            score = calculate_score(word, puzzle)
            color = "Blue" if len(set(word)) == 7 else "Black"
            sbg.add_word(f"{word} ({score})", color)
            found_words.add(word)
            total_score[0] += score
            update_score_message(found_words, total_score[0])
            sbg.set_field("Word", "")

    dictionary = read_dictionary()
    found_words = set()
    total_score = [0]  # Using a list to make it mutable

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action, 7)
    sbg.add_field("Word", word_action)
    sbg.add_button("Solve", solve_action)

# Startup code
if __name__ == "__main__":
    spelling_bee()