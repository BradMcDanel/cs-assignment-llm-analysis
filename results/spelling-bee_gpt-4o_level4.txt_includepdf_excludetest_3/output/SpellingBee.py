from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

def is_valid_puzzle(puzzle):
    # Check if the puzzle has exactly seven unique letters
    return len(puzzle) == 7 and len(set(puzzle)) == 7 and puzzle.isalpha()

def load_dictionary(file_path):
    # Load the dictionary and return as a set for quick lookup
    with open(file_path, 'r') as file:
        return set(word.strip() for word in file)

def find_valid_words(puzzle, dictionary):
    center_letter = puzzle[0]
    other_letters = set(puzzle)
    valid_words = []
    for word in dictionary:
        if len(word) >= 4 and center_letter in word and set(word).issubset(other_letters):
            valid_words.append(word)
    return valid_words

def calculate_score(word, is_pangram):
    if len(word) == 4:
        return 1
    score = len(word)
    if is_pangram:
        score += 7
    return score

def spelling_bee():
    dictionary = load_dictionary(DICTIONARY_FILE)
    
    def puzzle_action(s):
        if not is_valid_puzzle(s):
            sbg.show_message("Puzzle must have exactly 7 unique letters.", "Red")
            return
        sbg.set_beehive_letters(s.upper())
        sbg.show_message("Puzzle is set!", "Green")
    
    def solve_action(s):
        sbg.clear_word_list()  # Clear previous words
        puzzle = sbg.get_beehive_letters().lower()  # Get the current beehive letters
        if not puzzle or len(puzzle) != 7:
            sbg.show_message("Set a valid puzzle first!", "Red")
            return
        
        valid_words = find_valid_words(puzzle, dictionary)
        total_score = 0
        for word in valid_words:
            is_pangram = len(set(word)) == 7
            score = calculate_score(word, is_pangram)
            color = "Blue" if is_pangram else "Black"
            sbg.add_word(f"{word} ({score})", color)
            total_score += score
        
        sbg.show_message(f"Total words: {len(valid_words)}, Total score: {total_score}", "Green")
    
    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

# Startup code
if __name__ == "__main__":
    spelling_bee()