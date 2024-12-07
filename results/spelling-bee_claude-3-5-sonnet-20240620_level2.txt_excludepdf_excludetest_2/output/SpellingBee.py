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
            sbg.show_message("Invalid puzzle. Must be 7 unique letters.", "Red")

    def solve_action(s):
        sbg.clear_word_list()
        words = find_valid_words(sbg.get_beehive_letters().lower(), dictionary)
        display_words(words)
        show_score(len(words), calculate_total_score(words))

    def word_action(s):
        word = s.lower()
        if word in found_words:
            sbg.show_message(f"{word} already found!", "Red")
        elif is_valid_word(word, sbg.get_beehive_letters().lower(), dictionary):
            score = calculate_word_score(word, sbg.get_beehive_letters())
            found_words.add(word)
            sbg.add_word(f"{word} ({score})", "Blue" if is_pangram(word, sbg.get_beehive_letters()) else "Black")
            nonlocal total_score
            total_score += score
            sbg.show_message(f"Good! {len(found_words)} words, {total_score} points.")
            sbg.set_field("Word", "")
        else:
            sbg.show_message(get_invalid_reason(word, sbg.get_beehive_letters().lower(), dictionary), "Red")

    sbg.add_field("Puzzle", puzzle_action, 7)
    sbg.add_button("Solve", solve_action)
    sbg.add_field("Word", word_action)

def load_dictionary(filename):
    with open(filename, 'r') as f:
        return set(word.strip().lower() for word in f)

def is_valid_puzzle(puzzle):
    return len(puzzle) == 7 and puzzle.isalpha() and len(set(puzzle)) == 7

def is_valid_word(word, puzzle, dictionary):
    return (len(word) >= 4 and
            set(word).issubset(set(puzzle)) and
            puzzle[0] in word and
            word in dictionary)

def find_valid_words(puzzle, dictionary):
    return [word for word in dictionary if is_valid_word(word, puzzle, dictionary)]

def calculate_word_score(word, puzzle):
    base_score = len(word) if len(word) > 4 else 1
    return base_score + (7 if is_pangram(word, puzzle) else 0)

def is_pangram(word, puzzle):
    return set(word) == set(puzzle.lower())

def calculate_total_score(words):
    return sum(calculate_word_score(word, set(word)) for word in words)

def display_words(words):
    for word in sorted(words):
        score = calculate_word_score(word, set(word))
        sbg.add_word(f"{word} ({score})", "Blue" if is_pangram(word, set(word)) else "Black")

def show_score(word_count, total_score):
    sbg.show_message(f"Found {word_count} words. Total score: {total_score} points.")

def get_invalid_reason(word, puzzle, dictionary):
    if len(word) < 4:
        return "Word must be at least 4 letters long."
    if not set(word).issubset(set(puzzle)):
        return "Word contains letters not in the puzzle."
    if puzzle[0] not in word:
        return "Word must contain the center letter."
    if word not in dictionary:
        return "Word not in dictionary."

if __name__ == "__main__":
    spelling_bee()