from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

def spelling_bee():
    # Load the dictionary from file
    with open(DICTIONARY_FILE, 'r') as file:
        dictionary = set(file.read().strip().split('\n'))

    def is_legal_puzzle(puzzle):
        """Checks if the puzzle input is a legal configuration."""
        if len(puzzle) != 7:
            sbg.show_message("Puzzle must be exactly 7 letters.", "Red")
            return False
        if not puzzle.isalpha():
            sbg.show_message("Puzzle must only contain letters.", "Red")
            return False
        if len(set(puzzle)) != 7:
            sbg.show_message("Letters must not repeat.", "Red")
            return False
        return True

    def puzzle_action(s):
        """Handles the action when a puzzle is entered."""
        if is_legal_puzzle(s):
            sbg.set_beehive_letters(s.upper())
            sbg.show_message("Puzzle set successfully.", "Green")
        else:
            sbg.set_field("Puzzle", "")

    def solve_action(s):
        """Solves the puzzle and displays all valid words."""
        sbg.clear_word_list()
        beehive_letters = sbg.get_beehive_letters().lower()
        center_letter = beehive_letters[0]
        valid_words = []

        for word in dictionary:
            if len(word) >= 4 and center_letter in word and all(c in beehive_letters for c in word):
                valid_words.append(word)

        total_score = 0
        for word in valid_words:
            word_score = len(word)
            if len(set(word)) == 7:
                word_score += 7
                sbg.add_word(f"{word} ({word_score})", "Blue")
            else:
                sbg.add_word(f"{word} ({word_score})")
            total_score += word_score

        sbg.show_message(f"Total Score: {total_score}, Words Found: {len(valid_words)}", "Black")

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

# Startup code
if __name__ == "__main__":
    spelling_bee()