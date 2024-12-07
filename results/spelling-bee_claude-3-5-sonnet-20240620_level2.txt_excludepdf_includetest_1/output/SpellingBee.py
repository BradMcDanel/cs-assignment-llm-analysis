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
            sbg.show_message("Puzzle set! Click 'Solve' or enter words.", "Green")
        else:
            sbg.show_message("Invalid puzzle. Enter 7 unique letters.", "Red")

    def solve_action(s):
        words = find_valid_words(sbg.get_beehive_letters().lower(), dictionary)
        display_words(words)
        show_score(len(words), calculate_total_score(words))

    def word_action(s):
        word = s.lower()
        if is_valid_word(word, sbg.get_beehive_letters().lower(), dictionary, found_words):
            score = calculate_word_score(word)
            found_words.add(word)
            total_score += score
            sbg.add_word(word, "Blue" if is_pangram(word, sbg.get_beehive_letters()) else "Black")
            sbg.set_field("Word", "")
            show_score(len(found_words), total_score)
        else:
            show_error_message(word, sbg.get_beehive_letters().lower(), dictionary, found_words)

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
    center = puzzle[0]
    return [word for word in dictionary if 
            len(word) >= 4 and 
            center in word and 
            all(letter in puzzle for letter in word)]

def is_valid_word(word, puzzle, dictionary, found_words):
    return (word in dictionary and
            len(word) >= 4 and
            puzzle[0] in word and
            all(letter in puzzle for letter in word) and
            word not in found_words)

def is_pangram(word, puzzle):
    return set(word) == set(puzzle.lower())

def calculate_word_score(word):
    base_score = len(word) if len(word) > 4 else 1
    return base_score + (7 if is_pangram(word, word) else 0)

def calculate_total_score(words):
    return sum(calculate_word_score(word) for word in words)

def display_words(words):
    sbg.clear_word_list()
    for word in sorted(words):
        score = calculate_word_score(word)
        color = "Blue" if is_pangram(word, sbg.get_beehive_letters()) else "Black"
        sbg.add_word(f"{word} ({score})", color)

def show_score(word_count, total_score):
    sbg.show_message(f"Words: {word_count}, Score: {total_score}", "Green")

def show_error_message(word, puzzle, dictionary, found_words):
    if word in found_words:
        sbg.show_message("Word already found", "Red")
    elif len(word) < 4:
        sbg.show_message("Word too short", "Red")
    elif puzzle[0] not in word:
        sbg.show_message("Missing center letter", "Red")
    elif not all(letter in puzzle for letter in word):
        sbg.show_message("Invalid letters used", "Red")
    elif word not in dictionary:
        sbg.show_message("Word not in dictionary", "Red")

if __name__ == "__main__":
    spelling_bee()