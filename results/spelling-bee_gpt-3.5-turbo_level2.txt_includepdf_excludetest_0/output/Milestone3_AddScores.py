# Your code for Milestone 3: Add scores to the display

from SpellingBeeGraphics import SpellingBeeGraphics

def solve_action(s):
    puzzle = sbg.get_beehive_letters()
    words = read_dictionary(DICTIONARY_FILE)
    total_score = 0
    word_count = 0
    
    for word in words:
        if is_legal_word(word, puzzle):
            score = calculate_score(word)
            sbg.add_word(f"{word} ({score})")
            total_score += score
            word_count += 1
            
    sbg.show_message(f"Total words found: {word_count}, Total score: {total_score}")

def calculate_score(word):
    if len(word) == 4:
        return 1
    else:
        return len(word)

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

# Startup code
sbg = SpellingBeeGraphics()
sbg.add_field("Puzzle", puzzle_action)
sbg.add_button("Solve", solve_action)