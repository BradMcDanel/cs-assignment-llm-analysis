from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

# Starter program

def spelling_bee():
    def puzzle_action(s):
        if is_legal_puzzle(s):
            sbg.set_beehive_letters(s)
            sbg.show_message("Puzzle set successfully", "Green")
        else:
            sbg.show_message("Invalid puzzle. Ensure it has 7 unique letters.", "Red")

    def solve_action(s):
        sbg.clear_word_list()
        puzzle = sbg.get_beehive_letters()
        center_letter = puzzle[0]
        valid_words = find_valid_words(puzzle, center_letter)
        for word in valid_words:
            if is_pangram(word, puzzle):
                sbg.add_word(word, "Blue")
            else:
                sbg.add_word(word, "Black")
        score_message = f"Total words: {len(valid_words)} - Total score: {calculate_score(valid_words)}"
        sbg.show_message(score_message, "Green")

    # Initialize graphics
    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

def is_legal_puzzle(puzzle):
    if len(puzzle) != 7:
        return False
    if not all(char.isalpha() for char in puzzle):
        return False
    if len(set(puzzle)) != 7:
        return False
    return True

def read_dictionary():
    with open(DICTIONARY_FILE, 'r') as file:
        return [line.strip() for line in file]

def find_valid_words(puzzle, center_letter):
    dictionary = read_dictionary()
    valid_words = []
    for word in dictionary:
        if len(word) >= 4 and center_letter in word and all(char in puzzle for char in word):
            valid_words.append(word)
    return valid_words

def is_pangram(word, puzzle):
    return set(word) == set(puzzle)

def calculate_score(words):
    score = 0
    for word in words:
        if len(word) == 4:
            score += 1
        else:
            score += len(word)
        if is_pangram(word, sbg.get_beehive_letters()):
            score += 7
    return score

# Startup code
if __name__ == "__main__":
    spelling_bee()

### EnglishWords.txt - PROVIDED ###