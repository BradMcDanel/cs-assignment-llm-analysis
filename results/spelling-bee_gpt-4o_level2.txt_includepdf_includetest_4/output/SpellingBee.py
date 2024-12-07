"""
This file is the solution for the SpellingBee project.
"""

from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

def spelling_bee():
    dictionary = load_dictionary()

    def puzzle_action(puzzle):
        puzzle = puzzle.strip().upper()
        if is_valid_puzzle(puzzle):
            sbg.set_beehive_letters(puzzle)
            sbg.show_message("")
        else:
            sbg.show_message("Invalid puzzle! Ensure it is 7 unique letters.", "Red")

    def solve_action(_):
        sbg.clear_word_list()
        beehive_letters = sbg.get_beehive_letters()
        center_letter = beehive_letters[0]
        found_words = []

        for word in dictionary:
            if is_valid_word(word, beehive_letters, center_letter):
                score = calculate_score(word, beehive_letters)
                color = "Blue" if is_pangram(word, beehive_letters) else "Black"
                sbg.add_word(f"{word} ({score})", color)
                found_words.append(word)

        total_score = sum(calculate_score(word, beehive_letters) for word in found_words)
        sbg.show_message(f"Total words: {len(found_words)}, Total score: {total_score}")

    def word_action(word):
        word = word.strip().lower()
        beehive_letters = sbg.get_beehive_letters()
        center_letter = beehive_letters[0]
        found_words = set(sbg.get_field("Word").split())

        if word in found_words:
            sbg.show_message(f"Word '{word}' already found!", "Red")
        elif word not in dictionary:
            sbg.show_message(f"Word '{word}' is not in the dictionary!", "Red")
        elif not is_valid_word(word, beehive_letters, center_letter):
            sbg.show_message(f"Word '{word}' is not valid for this puzzle!", "Red")
        else:
            score = calculate_score(word, beehive_letters)
            color = "Blue" if is_pangram(word, beehive_letters) else "Black"
            sbg.add_word(f"{word} ({score})", color)
            sbg.set_field("Word", f"{' '.join(found_words.union({word}))}")

    def is_valid_puzzle(puzzle):
        return len(puzzle) == 7 and puzzle.isalpha() and len(set(puzzle)) == 7

    def is_valid_word(word, beehive_letters, center_letter):
        return (
            len(word) >= 4 and
            center_letter in word and
            all(char in beehive_letters for char in word)
        )

    def is_pangram(word, beehive_letters):
        return all(letter in word for letter in beehive_letters.lower())

    def calculate_score(word, beehive_letters):
        score = len(word) if len(word) > 4 else 1
        if is_pangram(word, beehive_letters):
            score += 7
        return score

    def load_dictionary():
        with open(DICTIONARY_FILE, "r") as file:
            return {line.strip().lower() for line in file}

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)
    sbg.add_field("Word", word_action)

# Startup code
if __name__ == "__main__":
    spelling_bee()