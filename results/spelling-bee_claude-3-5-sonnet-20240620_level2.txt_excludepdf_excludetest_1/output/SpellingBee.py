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
            sbg.show_message("Puzzle set! Click Solve or enter words.", "Green")
        else:
            sbg.show_message("Invalid puzzle. Enter 7 unique letters.", "Red")

    def solve_action(s):
        words = find_valid_words(sbg.get_beehive_letters().lower(), dictionary)
        display_words(words)
        show_score(len(words), calculate_total_score(words))

    def word_action(s):
        word = s.lower()
        center_letter = sbg.get_beehive_letters()[0].lower()
        if is_valid_word(word, sbg.get_beehive_letters().lower(), center_letter, dictionary):
            if word not in found_words:
                found_words.add(word)
                score = calculate_word_score(word, sbg.get_beehive_letters())
                display_word(word, score)
                nonlocal total_score
                total_score += score
                show_score(len(found_words), total_score)
                sbg.set_field("Word", "")
            else:
                sbg.show_message("Word already found!", "Red")
        else:
            show_error_message(word, sbg.get_beehive_letters().lower(), center_letter, dictionary)

    sbg.add_field("Puzzle", puzzle_action, 7)
    sbg.add_button("Solve", solve_action)
    sbg.add_field("Word", word_action)

def load_dictionary(filename):
    with open(filename, 'r') as f:
        return set(word.strip().lower() for word in f)

def is_valid_puzzle(puzzle):
    return (len(puzzle) == 7 and
            puzzle.isalpha() and
            len(set(puzzle)) == 7)

def find_valid_words(puzzle, dictionary):
    center_letter = puzzle[0]
    return [word for word in dictionary if is_valid_word(word, puzzle, center_letter, dictionary)]

def is_valid_word(word, puzzle, center_letter, dictionary):
    return (len(word) >= 4 and
            center_letter in word and
            set(word).issubset(set(puzzle)) and
            word in dictionary)

def calculate_word_score(word, puzzle):
    score = len(word) if len(word) > 4 else 1
    if set(word) == set(puzzle):
        score += 7  # Pangram bonus
    return score

def calculate_total_score(words):
    return sum(calculate_word_score(word, set(word)) for word in words)

def display_words(words):
    sbg.clear_word_list()
    for word in sorted(words):
        display_word(word, calculate_word_score(word, set(word)))

def display_word(word, score):
    color = "Blue" if len(set(word)) == 7 else "Black"
    sbg.add_word(f"{word} ({score})", color)

def show_score(word_count, total_score):
    sbg.show_message(f"Words: {word_count}, Score: {total_score}", "Green")

def show_error_message(word, puzzle, center_letter, dictionary):
    if len(word) < 4:
        sbg.show_message("Word must be at least 4 letters long.", "Red")
    elif not set(word).issubset(set(puzzle)):
        sbg.show_message("Word contains letters not in the puzzle.", "Red")
    elif center_letter not in word:
        sbg.show_message("Word must contain the center letter.", "Red")
    elif word not in dictionary:
        sbg.show_message("Word not in dictionary.", "Red")

# Startup code
if __name__ == "__main__":
    spelling_bee()