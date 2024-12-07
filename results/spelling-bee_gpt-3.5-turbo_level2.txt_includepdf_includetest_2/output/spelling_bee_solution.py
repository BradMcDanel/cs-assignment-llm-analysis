from SpellingBeeGraphics import SpellingBeeGraphics

DICTIONARY_FILE = "EnglishWords.txt"

def spelling_bee():
    def puzzle_action(s):
        puzzle = sbg.get_field("Puzzle")
        if is_valid_puzzle(puzzle):
            sbg.set_beehive_letters(puzzle)
        else:
            sbg.show_message("Invalid puzzle. Please enter exactly 7 unique letters.", "Red")

    def solve_action(s):
        puzzle_letters = sbg.get_beehive_letters()
        words = read_dictionary(DICTIONARY_FILE)
        valid_words = find_valid_words(puzzle_letters, words)
        display_words(valid_words)

    def is_valid_puzzle(puzzle):
        return len(puzzle) == 7 and len(set(puzzle)) == 7

    def read_dictionary(file):
        with open(file, 'r') as f:
            return set(word.strip().lower() for word in f)

    def find_valid_words(puzzle_letters, words):
        center_letter = puzzle_letters[0]
        valid_words = []
        for word in words:
            if len(word) >= 4 and all(letter in puzzle_letters for letter in word) and center_letter in word:
                valid_words.append(word)
        return valid_words

    def display_words(words):
        sbg.clear_word_list()
        total_score = 0
        pangram_found = False
        for word in words:
            score = len(word)
            if len(set(word)) == 7:
                score += 7
                pangram_found = True
            sbg.add_word(f"{word} ({score})", "Blue" if pangram_found else "Black")
            total_score += score
        sbg.show_message(f"Found {len(words)} words. Total score: {total_score}")

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

if __name__ == "__main__":
    spelling_bee()