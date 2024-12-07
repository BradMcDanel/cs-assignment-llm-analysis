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
            sbg.show_message("Puzzle set successfully!", "Green")
        else:
            sbg.show_message("Invalid puzzle. Please enter 7 unique letters.", "Red")

    def solve_action(s):
        puzzle = sbg.get_beehive_letters().lower()
        if not puzzle:
            sbg.show_message("Please set a puzzle first.", "Red")
            return
        
        sbg.clear_word_list()
        found_words.clear()
        nonlocal total_score
        total_score = 0
        
        for word in dictionary:
            if is_valid_word(word, puzzle):
                add_word(word)
        
        update_score_display()

    def word_action(s):
        puzzle = sbg.get_beehive_letters().lower()
        word = s.lower()
        
        if not puzzle:
            sbg.show_message("Please set a puzzle first.", "Red")
        elif word in found_words:
            sbg.show_message(f"'{word}' has already been found.", "Red")
        elif not is_valid_word(word, puzzle):
            sbg.show_message(f"'{word}' is not a valid word for this puzzle.", "Red")
        elif word not in dictionary:
            sbg.show_message(f"'{word}' is not in the dictionary.", "Red")
        else:
            add_word(word)
            update_score_display()
            sbg.set_field("Word", "")

    def add_word(word):
        score = calculate_score(word)
        color = "Blue" if is_pangram(word, sbg.get_beehive_letters().lower()) else "Black"
        sbg.add_word(f"{word} ({score})", color)
        found_words.add(word)
        nonlocal total_score
        total_score += score

    def update_score_display():
        sbg.show_message(f"Words: {len(found_words)}, Score: {total_score}", "Black")

    sbg.add_field("Puzzle", puzzle_action, 7)
    sbg.add_button("Solve", solve_action)
    sbg.add_field("Word", word_action)

def load_dictionary(filename):
    with open(filename, 'r') as f:
        return set(word.strip().lower() for word in f)

def is_valid_puzzle(puzzle):
    return len(puzzle) == 7 and puzzle.isalpha() and len(set(puzzle)) == 7

def is_valid_word(word, puzzle):
    return (len(word) >= 4 and
            set(word).issubset(set(puzzle)) and
            puzzle[0] in word)

def calculate_score(word):
    base_score = len(word) if len(word) > 4 else 1
    pangram_bonus = 7 if is_pangram(word, sbg.get_beehive_letters().lower()) else 0
    return base_score + pangram_bonus

def is_pangram(word, puzzle):
    return set(word) == set(puzzle)

if __name__ == "__main__":
    spelling_bee()