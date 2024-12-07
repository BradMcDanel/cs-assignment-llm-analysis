from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

def load_dictionary():
    """Loads the dictionary file into a set of words."""
    with open(DICTIONARY_FILE) as file:
        return set(line.strip().lower() for line in file)

def is_valid_puzzle(puzzle):
    """Validates the puzzle string."""
    if len(puzzle) != 7 or not puzzle.isalpha() or len(set(puzzle)) != 7:
        return False
    return True

def calculate_word_score(word, is_pangram):
    """Calculates the score for a given word."""
    score = len(word) if len(word) > 4 else 1
    if is_pangram:
        score += 7
    return score

def spelling_bee():
    dictionary = load_dictionary()

    def puzzle_action(s):
        if is_valid_puzzle(s):
            sbg.set_beehive_letters(s.upper())
            sbg.show_message("Puzzle set successfully.", "Green")
        else:
            sbg.show_message("Invalid puzzle. Must be 7 unique letters.", "Red")

    def solve_action(s):
        beehive_letters = sbg.get_beehive_letters().lower()
        center_letter = beehive_letters[0]
        valid_words = []

        for word in dictionary:
            if len(word) >= 4 and all(c in beehive_letters for c in word) and center_letter in word:
                is_pangram = all(c in word for c in beehive_letters)
                score = calculate_word_score(word, is_pangram)
                color = "Blue" if is_pangram else "Black"
                sbg.add_word(f"{word} ({score})", color)
                valid_words.append(word)

        sbg.show_message(f"Found {len(valid_words)} words.", "Green")

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

# Startup code
if __name__ == "__main__":
    spelling_bee()