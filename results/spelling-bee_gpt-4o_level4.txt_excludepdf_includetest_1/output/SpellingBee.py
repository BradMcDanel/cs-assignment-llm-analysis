from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

def spelling_bee():
    # Helper functions
    def is_legal_puzzle(puzzle):
        if len(puzzle) != 7:
            sbg.show_message("Puzzle must contain exactly 7 letters.", "Red")
            return False
        if not puzzle.isalpha():
            sbg.show_message("Puzzle must contain only letters.", "Red")
            return False
        if len(set(puzzle)) != 7:
            sbg.show_message("Puzzle must not contain duplicate letters.", "Red")
            return False
        return True

    def check_word_validity(word, beehive_letters, center_letter):
        if len(word) < 4:
            return False
        if center_letter not in word:
            return False
        for letter in word:
            if letter not in beehive_letters:
                return False
        return True

    def read_dictionary():
        with open(DICTIONARY_FILE, "r") as file:
            return set(file.read().splitlines())

    def puzzle_action(puzzle):
        puzzle = puzzle.upper()
        if is_legal_puzzle(puzzle):
            sbg.set_beehive_letters(puzzle)
            sbg.show_message("Puzzle updated.", "Green")

    def solve_action(s):
        sbg.clear_word_list()  # Clear previous words
        beehive_letters = sbg.get_beehive_letters()
        center_letter = beehive_letters[0]
        legal_words = read_dictionary()

        score = 0
        word_count = 0

        for word in legal_words:
            if check_word_validity(word, beehive_letters, center_letter):
                word_count += 1
                word_score = len(word) if len(word) > 4 else 1
                if set(word) == set(beehive_letters):
                    word_score += 7  # Pangram bonus
                    sbg.add_word(word, "Blue")
                else:
                    sbg.add_word(word, "Black")
                score += word_score

        sbg.show_message(f"Found {word_count} words with a total score of {score}.", "Green")

    # Initialize the graphics
    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

# Startup code
if __name__ == "__main__":
    spelling_bee()