"""
This file is the complete solution for the SpellingBee project.
"""

from SpellingBeeGraphics import SpellingBeeGraphics

# Constants

DICTIONARY_FILE = "EnglishWords.txt"

def load_dictionary():
    """Load the dictionary from the file into a set."""
    with open(DICTIONARY_FILE, 'r') as file:
        return set(word.strip() for word in file)

def is_valid_puzzle(letters):
    """Checks if the provided letters form a valid puzzle."""
    if len(letters) != 7:
        return False, "The puzzle must contain exactly seven characters."
    if not all(letter.isalpha() for letter in letters):
        return False, "Every character must be a letter."
    if len(set(letters)) != 7:
        return False, "Each letter must be unique."
    return True, ""

def is_valid_word(word, beehive_letters, center_letter):
    """Checks if a word is valid according to the rules."""
    if len(word) < 4:
        return False, "The word is too short."
    if center_letter not in word:
        return False, "The word must include the center letter."
    if not all(letter in beehive_letters for letter in word):
        return False, "The word contains invalid letters."
    return True, ""

def calculate_word_score(word, is_pangram):
    """Calculates the score for a given word."""
    score = len(word) if len(word) > 4 else 1
    if is_pangram:
        score += 7
    return score

def spelling_bee():
    dictionary = load_dictionary()

    def puzzle_action(puzzle):
        puzzle = puzzle.upper()
        valid, message = is_valid_puzzle(puzzle)
        if not valid:
            sbg.show_message(message, "Red")
        else:
            sbg.set_beehive_letters(puzzle)
            sbg.show_message("Puzzle set successfully!", "Green")

    def solve_action(_):
        sbg.clear_word_list()
        beehive_letters = sbg.get_beehive_letters()
        center_letter = beehive_letters[0]
        words_found = []
        total_score = 0

        for word in dictionary:
            if is_valid_word(word, beehive_letters, center_letter)[0]:
                is_pangram = len(set(word)) == 7
                score = calculate_word_score(word, is_pangram)
                total_score += score
                color = "Blue" if is_pangram else "Black"
                sbg.add_word(f"{word} ({score})", color)
                words_found.append(word)

        sbg.show_message(f"Total words: {len(words_found)}, Total score: {total_score}", "Black")

    def word_action(word):
        word = word.lower()
        beehive_letters = sbg.get_beehive_letters().lower()
        center_letter = beehive_letters[0]
        if word in words_found:
            sbg.show_message("Word already found!", "Red")
        elif word not in dictionary:
            sbg.show_message("Word not in dictionary!", "Red")
        else:
            valid, message = is_valid_word(word, beehive_letters, center_letter)
            if not valid:
                sbg.show_message(message, "Red")
            else:
                is_pangram = len(set(word)) == 7
                score = calculate_word_score(word, is_pangram)
                total_score += score
                color = "Blue" if is_pangram else "Black"
                sbg.add_word(f"{word} ({score})", color)
                words_found.append(word)
                sbg.show_message(f"Word added! Total score: {total_score}", "Green")
                sbg.set_field("Word", "")

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)
    sbg.add_field("Word", word_action)

# Startup code

if __name__ == "__main__":
    spelling_bee()