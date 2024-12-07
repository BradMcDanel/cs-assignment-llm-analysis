from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

def load_dictionary():
    """Loads the dictionary file into a set for fast lookup."""
    with open(DICTIONARY_FILE) as file:
        return set(word.strip().lower() for word in file)

def is_legal_puzzle(puzzle):
    """Checks if the puzzle is legal according to the rules."""
    if len(puzzle) != 7:
        return "Puzzle must contain exactly seven characters."
    if not all(char.isalpha() for char in puzzle):
        return "Puzzle must contain only alphabetic characters."
    if len(set(puzzle)) != len(puzzle):
        return "Puzzle must not contain duplicate letters."
    return True

def is_valid_word(word, puzzle, center_letter):
    """Checks if a word is valid for the puzzle."""
    if len(word) < 4:
        return False
    if center_letter not in word:
        return False
    if any(char not in puzzle for char in word):
        return False
    return True

def calculate_score(word, is_pangram):
    """Calculates the score for a word."""
    score = len(word)
    if len(word) == 4:
        score = 1
    if is_pangram:
        score += 7
    return score

def spelling_bee():
    dictionary = load_dictionary()
    
    def puzzle_action(s):
        puzzle = s.strip().upper()
        legal_check = is_legal_puzzle(puzzle)
        if legal_check is True:
            sbg.set_beehive_letters(puzzle)
            sbg.show_message("")
        else:
            sbg.show_message(legal_check, "Red")

    def solve_action(s):
        sbg.clear_word_list()
        puzzle = sbg.get_beehive_letters().lower()
        center_letter = puzzle[0]
        found_words = []
        total_score = 0

        for word in dictionary:
            if is_valid_word(word, puzzle, center_letter):
                is_pangram = len(set(word)) == 7
                score = calculate_score(word, is_pangram)
                color = "Blue" if is_pangram else "Black"
                sbg.add_word(f"{word} ({score})", color)
                found_words.append(word)
                total_score += score
        
        sbg.show_message(f"Found {len(found_words)} words with a total score of {total_score}.")

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

if __name__ == "__main__":
    spelling_bee()