from SpellingBeeGraphics import SpellingBeeGraphics

DICTIONARY_FILE = "EnglishWords.txt"

def spelling_bee():
    sbg = SpellingBeeGraphics()
    dictionary = load_dictionary(DICTIONARY_FILE)
    found_words = set()
    total_score = 0

    def puzzle_action(s):
        if is_valid_puzzle(s):
            sbg.set_beehive_letters(s.upper())
            sbg.show_message("Puzzle set successfully!", "Green")
        else:
            sbg.show_message("Invalid puzzle. Please enter 7 unique letters.", "Red")

    def solve_action(s):
        puzzle = sbg.get_beehive_letters()
        if not puzzle:
            sbg.show_message("Please set a puzzle first.", "Red")
            return
        
        sbg.clear_word_list()
        words = find_valid_words(puzzle, dictionary)
        display_words(words)
        show_summary(words)

    def word_action(s):
        puzzle = sbg.get_beehive_letters()
        if not puzzle:
            sbg.show_message("Please set a puzzle first.", "Red")
            return
        
        word = s.lower()
        if is_valid_word(word, puzzle, dictionary):
            if word in found_words:
                sbg.show_message(f"'{word}' has already been found.", "Red")
            else:
                found_words.add(word)
                score = calculate_score(word, puzzle)
                display_word(word, score)
                update_score(score)
                sbg.set_field("Word", "")
        else:
            show_error_message(word, puzzle)

    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)
    sbg.add_field("Word", word_action)

def load_dictionary(filename):
    with open(filename, 'r') as file:
        return set(word.strip().lower() for word in file)

def is_valid_puzzle(s):
    return len(s) == 7 and s.isalpha() and len(set(s)) == 7

def find_valid_words(puzzle, dictionary):
    center = puzzle[0].lower()
    valid_words = []
    for word in dictionary:
        if len(word) >= 4 and center in word and set(word).issubset(set(puzzle.lower())):
            valid_words.append(word)
    return valid_words

def is_valid_word(word, puzzle, dictionary):
    center = puzzle[0].lower()
    return (len(word) >= 4 and
            center in word and
            set(word).issubset(set(puzzle.lower())) and
            word in dictionary)

def calculate_score(word, puzzle):
    score = len(word) if len(word) > 4 else 1
    if set(word) == set(puzzle.lower()):
        score += 7  # Pangram bonus
    return score

def display_words(words):
    for word in words:
        display_word(word, calculate_score(word, sbg.get_beehive_letters()))

def display_word(word, score):
    color = "Blue" if set(word) == set(sbg.get_beehive_letters().lower()) else "Black"
    sbg.add_word(f"{word} ({score})", color)

def show_summary(words):
    total_score = sum(calculate_score(word, sbg.get_beehive_letters()) for word in words)
    sbg.show_message(f"Found {len(words)} words. Total score: {total_score}", "Green")

def update_score(score):
    global total_score
    total_score += score
    sbg.show_message(f"Words found: {len(found_words)}. Total score: {total_score}", "Green")

def show_error_message(word, puzzle):
    if len(word) < 4:
        sbg.show_message("Word must be at least 4 letters long.", "Red")
    elif puzzle[0].lower() not in word:
        sbg.show_message(f"Word must contain the center letter '{puzzle[0]}'.", "Red")
    elif not set(word).issubset(set(puzzle.lower())):
        sbg.show_message("Word contains invalid letters.", "Red")
    else:
        sbg.show_message("Word not in dictionary.", "Red")

if __name__ == "__main__":
    spelling_bee()