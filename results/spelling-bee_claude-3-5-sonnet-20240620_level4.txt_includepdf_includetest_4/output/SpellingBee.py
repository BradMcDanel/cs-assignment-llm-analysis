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
        
        update_score_display()

    def word_action(s):
        letters = sbg.get_beehive_letters()
        if not letters:
            sbg.show_message("Please set a puzzle first.", "Red")
            return
        
        word = s.lower()
        if word in found_words:
            sbg.show_message(f"'{word}' has already been found.", "Red")
        elif not is_valid_word(word, letters):
            sbg.show_message(f"'{word}' is not a valid word for this puzzle.", "Red")
        else:
            add_word(word)
            update_score_display()
        
        sbg.set_field("Word", "")  # Clear the word field

    def add_word(word):
        score = calculate_score(word)
        color = "Blue" if is_pangram(word, sbg.get_beehive_letters()) else "Black"
        sbg.add_word(f"{word} ({score})", color)
        found_words.add(word)
        nonlocal total_score
        total_score += score

    def update_score_display():
        sbg.show_message(f"Words: {len(found_words)}, Score: {total_score}")

    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_field("Word", word_action)
    sbg.add_button("Solve", solve_action)

def load_dictionary(filename):
    with open(filename, 'r') as file:
        return set(word.strip().lower() for word in file if len(word.strip()) >= 4)

def is_valid_puzzle(s):
    return len(s) == 7 and s.isalpha() and len(set(s.lower())) == 7

def is_valid_word(word, letters):
    center_letter = letters[0].lower()
    letters_set = set(letters.lower())
    return (len(word) >= 4 and
            center_letter in word and
            all(letter in letters_set for letter in word))

def calculate_score(word):
    base_score = len(word) if len(word) > 4 else 1
    return base_score + (7 if is_pangram(word, sbg.get_beehive_letters()) else 0)

def is_pangram(word, letters):
    return set(word) == set(letters.lower())

if __name__ == "__main__":
    spelling_bee()