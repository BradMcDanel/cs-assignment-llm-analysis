from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

# Starter program
def spelling_bee():
    def puzzle_action(s):
        puzzle = sbg.get_field("Puzzle")
        if validate_puzzle(puzzle):
            sbg.set_beehive_letters(puzzle)
        else:
            sbg.show_message("Invalid puzzle format. Please enter exactly 7 unique letters from A to Z.", "Red")

    def solve_action(s):
        puzzle = sbg.get_beehive_letters()
        words = read_dictionary(DICTIONARY_FILE)
        valid_words = find_valid_words(puzzle, words)
        display_words(valid_words)

    def validate_puzzle(puzzle):
        if len(puzzle) != 7:
            return False
        if len(set(puzzle)) != 7:
            return False
        if not all(letter.isalpha() and letter.isupper() for letter in puzzle):
            return False
        return True

    def read_dictionary(file):
        with open(file, 'r') as f:
            return set(word.strip().lower() for word in f)

    def find_valid_words(puzzle, words):
        center_letter = puzzle[0].lower()
        valid_words = set()
        for word in words:
            if len(word) >= 4 and center_letter in word and all(letter in puzzle for letter in word):
                valid_words.add(word)
        return valid_words

    def display_words(words):
        sbg.clear_word_list()
        total_score = 0
        pangram_bonus = 7 if sbg.get_beehive_letters() in words else 0
        for word in words:
            score = len(word) + pangram_bonus
            sbg.add_word(word, "Blue" if score == 7 else "Black")
            total_score += score
        sbg.show_message(f"Total words found: {len(words)}, Total score: {total_score}", "Black")

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

if __name__ == "__main__":
    spelling_bee()