from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

def spelling_bee():
    sbg = SpellingBeeGraphics()
    words = load_dictionary(DICTIONARY_FILE)
    found_words = set()
    total_score = 0

    def puzzle_action(s):
        if is_valid_puzzle(s):
            sbg.set_beehive_letters(s.upper())
            sbg.show_message("Puzzle set successfully!")
        else:
            sbg.show_message("Invalid puzzle. Please enter 7 unique letters.", "Red")

    def solve_action(s):
        letters = sbg.get_beehive_letters()
        if not letters:
            sbg.show_message("Please set a puzzle first.", "Red")
            return
        
        sbg.clear_word_list()
        found_words.clear()
        nonlocal total_score
        total_score = 0
        
        for word in words:
            if is_valid_word(word, letters):
                add_word(word)
        
        show_summary()

    def word_action(s):
        letters = sbg.get_beehive_letters()
        if not letters:
            sbg.show_message("Please set a puzzle first.", "Red")
            return
        
        word = s.lower()
        if word in found_words:
            sbg.show_message(f"'{word}' has already been found.", "Red")
        elif is_valid_word(word, letters):
            add_word(word)
            show_summary()
            sbg.set_field("Word", "")
        else:
            show_invalid_word_message(word, letters)

    def add_word(word):
        score = calculate_score(word)
        color = "Blue" if is_pangram(word, sbg.get_beehive_letters()) else "Black"
        sbg.add_word(f"{word} ({score})", color)
        found_words.add(word)
        nonlocal total_score
        total_score += score

    def show_summary():
        sbg.show_message(f"Words: {len(found_words)}, Score: {total_score}")

    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)
    sbg.add_field("Word", word_action)

def load_dictionary(filename):
    with open(filename, 'r') as file:
        return set(word.strip().lower() for word in file)

def is_valid_puzzle(s):
    return len(s) == 7 and s.isalpha() and len(set(s)) == 7

def is_valid_word(word, letters):
    center_letter = letters[0].lower()
    letters_set = set(letters.lower())
    return (len(word) >= 4 and
            center_letter in word and
            all(char in letters_set for char in word))

def calculate_score(word):
    base_score = len(word) if len(word) > 4 else 1
    return base_score + (7 if is_pangram(word, sbg.get_beehive_letters()) else 0)

def is_pangram(word, letters):
    return set(word) == set(letters.lower())

def show_invalid_word_message(word, letters):
    if len(word) < 4:
        sbg.show_message("Word must be at least 4 letters long.", "Red")
    elif letters[0].lower() not in word:
        sbg.show_message(f"Word must contain the center letter '{letters[0]}'.", "Red")
    elif not all(char in letters.lower() for char in word):
        sbg.show_message("Word contains invalid letters.", "Red")
    else:
        sbg.show_message("Word not in dictionary.", "Red")

if __name__ == "__main__":
    spelling_bee()