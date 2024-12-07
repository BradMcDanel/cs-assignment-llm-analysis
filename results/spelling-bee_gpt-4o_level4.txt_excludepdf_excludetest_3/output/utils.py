def load_dictionary(file_path):
    """Load the dictionary from a text file into a set for fast lookup."""
    with open(file_path, 'r') as file:
        return set(word.strip().lower() for word in file)

def is_valid_puzzle(puzzle):
    """Check if the puzzle string is a valid Spelling Bee puzzle."""
    if len(puzzle) != 7:
        return "Puzzle must contain exactly seven letters."
    if any(not char.isalpha() for char in puzzle):
        return "Puzzle can only contain letters."
    if len(set(puzzle)) != 7:
        return "Puzzle must contain unique letters."
    return None

def is_valid_word(word, beehive_letters, center_letter):
    """Check if a word is valid according to Spelling Bee rules."""
    if len(word) < 4:
        return False
    if center_letter not in word:
        return False
    for char in word:
        if char not in beehive_letters:
            return False
    return True

def calculate_word_score(word, is_pangram):
    """Calculate the score of a word based on its length and pangram status."""
    score = len(word)
    if len(word) == 4:
        score = 1
    if is_pangram:
        score += 7
    return score

def find_words(dictionary, beehive_letters, center_letter):
    """Find all valid words in the dictionary for the given beehive letters."""
    valid_words = []
    for word in dictionary:
        if is_valid_word(word, beehive_letters, center_letter):
            is_pangram = len(set(word)) == 7
            score = calculate_word_score(word, is_pangram)
            valid_words.append((word, score, is_pangram))
    return valid_words