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
            sbg.show_message("Puzzle set! You can start finding words.", "Green")
        else:
            sbg.show_message("Invalid puzzle. Please enter 7 unique letters.", "Red")

    def solve_action(s):
        puzzle = sbg.get_beehive_letters()
        if not puzzle:
            sbg.show_message("Please set a puzzle first.", "Red")
            return
        
        sbg.clear_word_list()
        found_words.clear()
        nonlocal total_score
        total_score = 0
        
        for word in words:
            if is_valid_word(word, puzzle):
                add_word(word)
        
        sbg.show_message(f"Found {len(found_words)} words. Total score: {total_score}", "Blue")

    def word_action(s):
        puzzle = sbg.get_beehive_letters()
        if not puzzle:
            sbg.show_message("Please set a puzzle first.", "Red")
            return
        
        word = s.lower()
        if word in found_words:
            sbg.show_message("Word already found!", "Red")
        elif not word in words:
            sbg.show_message("Not in dictionary.", "Red")
        elif len(word) < 4:
            sbg.show_message("Word too short.", "Red")
        elif not is_valid_word(word, puzzle):
            sbg.show_message("Invalid word for this puzzle.", "Red")
        else:
            add_word(word)
            sbg.set_field("Word", "")
            sbg.show_message(f"Good! Found {len(found_words)} words. Score: {total_score}", "Green")

    def add_word(word):
        score = calculate_score(word)
        color = "Blue" if len(set(word)) == 7 else "Black"
        sbg.add_word(f"{word} ({score})", color)
        found_words.add(word)
        nonlocal total_score
        total_score += score

    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)
    sbg.add_field("Word", word_action)

def load_dictionary(filename):
    with open(filename, 'r') as file:
        return set(word.strip().lower() for word in file)

def is_valid_puzzle(puzzle):
    return len(puzzle) == 7 and puzzle.isalpha() and len(set(puzzle)) == 7

def is_valid_word(word, puzzle):
    center = puzzle[0].lower()
    puzzle_set = set(puzzle.lower())
    return (len(word) >= 4 and
            center in word and
            all(letter in puzzle_set for letter in word))

def calculate_score(word):
    base_score = len(word) if len(word) > 4 else 1
    return base_score + (7 if len(set(word)) == 7 else 0)

if __name__ == "__main__":
    spelling_bee()