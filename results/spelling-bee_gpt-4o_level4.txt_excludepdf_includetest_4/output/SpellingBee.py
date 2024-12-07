from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

def spelling_bee():
    def load_dictionary(file_path):
        """Load the dictionary file and return a set of words."""
        with open(file_path, 'r') as file:
            return set(word.strip().lower() for word in file)

    def is_legal_puzzle(puzzle):
        """Check if the puzzle is legal."""
        if len(puzzle) != 7:
            return "Puzzle must contain exactly seven characters."
        if not puzzle.isalpha():
            return "Puzzle must contain only letters."
        if len(set(puzzle)) != 7:
            return "Puzzle must not contain duplicate letters."
        return True

    def puzzle_action(puzzle):
        """Handle the puzzle action when puzzle field is updated."""
        puzzle = puzzle.upper()
        legal_check = is_legal_puzzle(puzzle)
        if legal_check is True:
            sbg.set_beehive_letters(puzzle)
            sbg.show_message("")
        else:
            sbg.show_message(legal_check, "Red")

    def solve_action(s):
        """Solve the puzzle by finding all valid words."""
        sbg.clear_word_list()
        puzzle = sbg.get_beehive_letters().lower()
        center_letter = puzzle[0]
        legal_words = []
        total_score = 0

        for word in dictionary:
            if (len(word) >= 4 and center_letter in word and
                all(letter in puzzle for letter in word)):
                score = len(word) + (7 if len(set(word)) == 7 else 0)
                total_score += score
                sbg.add_word(word, "Blue" if score > len(word) else "Black")
                legal_words.append(word)

        sbg.show_message(f"Found {len(legal_words)} words with total score {total_score}.")

    # Load the dictionary once at the start
    dictionary = load_dictionary(DICTIONARY_FILE)
    
    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

# Startup code
if __name__ == "__main__":
    spelling_bee()