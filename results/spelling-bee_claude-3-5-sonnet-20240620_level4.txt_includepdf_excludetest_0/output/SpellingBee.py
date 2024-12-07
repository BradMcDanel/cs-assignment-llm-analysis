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
            sbg.set_beehive_letters(s)
            sbg.show_message("Puzzle set successfully!", "Green")
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
        elif word not in words:
            sbg.show_message("Not in dictionary.", "Red")
        elif len(word) < 4:
            sbg.show_message("Word too short.", "Red")
        elif not set(word).issubset(set(puzzle.lower())):
            sbg.show_message("Invalid letters used.", "Red")
        elif puzzle[0].lower() not in word:
            sbg.show_message("Center letter not used.", "Red")
        else:
            add_word(word)
            sbg.set_field("Word", "")
            sbg.show_message(f"Good! Score: {calculate_score(word)}", "Green")

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

def is_valid_puzzle(s):
    return len(s) == 7 and s.isalpha() and len(set(s)) == 7

def is_valid_word(word, puzzle):
    return (len(word) >= 4 and
            set(word).issubset(set(puzzle.lower())) and
            puzzle[0].lower() in word)

def calculate_score(word):
    base_score = len(word) if len(word) > 4 else 1
    pangram_bonus = 7 if len(set(word)) == 7 else 0
    return base_score + pangram_bonus

if __name__ == "__main__":
    spelling_bee()