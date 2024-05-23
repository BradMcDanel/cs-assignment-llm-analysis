from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

# Helper functions

def load_dictionary(file_path):
    """Loads the dictionary words from the specified file into a set."""
    with open(file_path, 'r') as file:
        return set(word.strip().lower() for word in file)

def is_legal_puzzle(puzzle):
    """Checks if the puzzle meets the criteria of having exactly 7 unique letters."""
    if len(puzzle) != 7:
        return "Puzzle must contain exactly seven characters."
    if not puzzle.isalpha():
        return "Puzzle must only contain alphabetical characters."
    if len(set(puzzle)) != 7:
        return "Puzzle must not contain duplicate characters."
    return None

def is_valid_word(word, letters, center_letter):
    """Checks if a word is valid based on the puzzle rules."""
    if len(word) < 4:
        return False
    if center_letter not in word:
        return False
    for letter in word:
        if letter not in letters:
            return False
    return True

def calculate_score(word, is_pangram):
    """Calculates the score of a word."""
    score = len(word)
    if len(word) == 4:
        score = 1
    if is_pangram:
        score += 7
    return score

# Milestone #1: Initialize the beehive with the letters in the puzzle field
def spelling_bee():
    dictionary = load_dictionary(DICTIONARY_FILE)
    
    def puzzle_action(s):
        error_msg = is_legal_puzzle(s)
        if error_msg:
            sbg.show_message(error_msg, "Red")
        else:
            sbg.set_beehive_letters(s)
            sbg.show_message("Puzzle set successfully!", "Green")
    
    def solve_action(s):
        sbg.clear_word_list()
        letters = sbg.get_beehive_letters().lower()
        center_letter = letters[0]
        words_found = []
        total_score = 0
        
        for word in dictionary:
            if is_valid_word(word, letters, center_letter):
                is_pangram = set(word) == set(letters)
                score = calculate_score(word, is_pangram)
                total_score += score
                color = "Blue" if is_pangram else "Black"
                sbg.add_word(f"{word} ({score})", color)
                words_found.append(word)
        
        sbg.show_message(f"Found {len(words_found)} words with total score {total_score}", "Green")
    
    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

# Startup code
if __name__ == "__main__":
    spelling_bee()