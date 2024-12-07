from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

def spelling_bee():
    sbg = SpellingBeeGraphics()
    dictionary = load_dictionary(DICTIONARY_FILE)
    found_words = set()
    total_score = 0
    
    def puzzle_action(s):
        if is_valid_puzzle(s):
            sbg.set_beehive_letters(s.upper())
            sbg.show_message("Puzzle set! Click Solve or enter words.")
        else:
            sbg.show_message("Invalid puzzle. Enter 7 unique letters.", "Red")

    def solve_action(s):
        words = find_valid_words(sbg.get_beehive_letters(), dictionary)
        display_words(words)
        show_score(len(words), calculate_total_score(words))

    def word_action(s):
        word = s.lower()
        center_letter = sbg.get_beehive_letters()[0].lower()
        if word in found_words:
            sbg.show_message(f"{word} has already been found.", "Red")
        elif is_valid_word(word, sbg.get_beehive_letters(), center_letter, dictionary):
            score = calculate_word_score(word, sbg.get_beehive_letters())
            found_words.add(word)
            nonlocal total_score
            total_score += score
            sbg.add_word(word, "Blue" if is_pangram(word, sbg.get_beehive_letters()) else "Black")
            sbg.set_field("Word", "")
            show_score(len(found_words), total_score)
        else:
            sbg.show_message(get_error_message(word, sbg.get_beehive_letters(), center_letter, dictionary), "Red")

    sbg.add_field("Puzzle", puzzle_action, 7)
    sbg.add_button("Solve", solve_action)
    sbg.add_field("Word", word_action)

def load_dictionary(filename):
    with open(filename, 'r') as file:
        return set(word.strip().lower() for word in file)

def is_valid_puzzle(puzzle):
    return len(puzzle) == 7 and puzzle.isalpha() and len(set(puzzle)) == 7

def find_valid_words(puzzle, dictionary):
    center_letter = puzzle[0].lower()
    return [word for word in dictionary if is_valid_word(word, puzzle, center_letter, dictionary)]

def is_valid_word(word, puzzle, center_letter, dictionary):
    return (len(word) >= 4 and
            center_letter in word and
            set(word).issubset(set(puzzle.lower())) and
            word in dictionary)

def get_error_message(word, puzzle, center_letter, dictionary):
    if len(word) < 4:
        return "Word must be at least 4 letters long."
    if center_letter not in word:
        return f"Word must contain the center letter '{center_letter}'."
    if not set(word).issubset(set(puzzle.lower())):
        return "Word contains letters not in the puzzle."
    if word not in dictionary:
        return "Word is not in the dictionary."
    return "Invalid word."

def calculate_word_score(word, puzzle):
    base_score = len(word) if len(word) > 4 else 1
    return base_score + (7 if is_pangram(word, puzzle) else 0)

def is_pangram(word, puzzle):
    return set(word) == set(puzzle.lower())

def calculate_total_score(words):
    return sum(calculate_word_score(word, set(word)) for word in words)

def display_words(words):
    sbg.clear_word_list()
    for word in sorted(words):
        score = calculate_word_score(word, set(word))
        color = "Blue" if is_pangram(word, set(word)) else "Black"
        sbg.add_word(f"{word} ({score})", color)

def show_score(word_count, total_score):
    sbg.show_message(f"Words: {word_count}, Score: {total_score}")

# Startup code
if __name__ == "__main__":
    spelling_bee()