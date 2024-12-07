from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

def spelling_bee():

    def load_dictionary():
        """Loads the words from the dictionary file into a set."""
        with open(DICTIONARY_FILE, 'r') as file:
            return set(word.strip().lower() for word in file)

    def is_legal_puzzle(puzzle):
        """Checks if the puzzle string is valid."""
        if len(puzzle) != 7:
            return "Puzzle must contain exactly seven letters."
        if not puzzle.isalpha():
            return "Puzzle must contain only alphabetic characters."
        if len(set(puzzle)) != 7:
            return "Puzzle must not have duplicate letters."
        return None

    def puzzle_action(puzzle):
        """Handles the action for setting the puzzle."""
        puzzle = puzzle.strip().lower()
        error_message = is_legal_puzzle(puzzle)
        if error_message:
            sbg.show_message(error_message, "Red")
        else:
            sbg.set_beehive_letters(puzzle)
            sbg.show_message("Puzzle set successfully.", "Green")

    def solve_action(button_name):
        """Solves the puzzle by finding all valid words."""
        words = load_dictionary()
        beehive_letters = sbg.get_beehive_letters().lower()
        center_letter = beehive_letters[0]
        valid_words = []

        for word in words:
            if len(word) >= 4 and center_letter in word and all(char in beehive_letters for char in word):
                valid_words.append(word)
        
        sbg.clear_word_list()
        total_score = 0
        for word in valid_words:
            score = len(word) if len(word) > 4 else 1
            is_pangram = set(beehive_letters) <= set(word)
            if is_pangram:
                score += 7
            total_score += score
            sbg.add_word(f"{word} ({score})", "Blue" if is_pangram else "Black")

        sbg.show_message(f"Total words found: {len(valid_words)}, Total score: {total_score}", "Black")

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

# Startup code
if __name__ == "__main__":
    spelling_bee()