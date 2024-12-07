import string
from collections import Counter

DICTIONARY_FILE = "EnglishWords.txt"

def load_dictionary(file):
    with open(file, 'r') as f:
        return set(word.strip().lower() for word in f)

def is_legal_puzzle(puzzle):
    if len(puzzle) != 7:
        return False
    if any(letter not in string.ascii_lowercase for letter in puzzle):
        return False
    if any(count > 1 for count in Counter(puzzle).values()):
        return False
    return True

def find_words_in_puzzle(puzzle, dictionary):
    center = puzzle[0]
    valid_words = set()

    for word in dictionary:
        if len(word) < 4:
            continue
        if center not in word:
            continue
        if set(word) - set(puzzle) != set():
            continue
        valid_words.add(word)

    return valid_words

def calculate_score(word):
    score = len(word)
    if len(word) == 7:
        score += 7
    return score

def main():
    dictionary = load_dictionary(DICTIONARY_FILE)

    def puzzle_action(puzzle):
        if is_legal_puzzle(puzzle):
            sbg.set_beehive_letters(puzzle.upper())
        else:
            sbg.show_message("Invalid puzzle. Please enter a valid 7-letter puzzle.", "Red")

    def solve_action(button_name):
        puzzle = sbg.get_beehive_letters().lower()
        valid_words = find_words_in_puzzle(puzzle, dictionary)

        sbg.clear_word_list()
        total_score = 0
        for word in valid_words:
            score = calculate_score(word)
            total_score += score
            color = "Blue" if len(word) == 7 else "Black"
            sbg.add_word(f"{word} ({score})", color)

        sbg.show_message(f"Found {len(valid_words)} words with a total score of {total_score}", "Black")

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

if __name__ == "__main__":
    main()