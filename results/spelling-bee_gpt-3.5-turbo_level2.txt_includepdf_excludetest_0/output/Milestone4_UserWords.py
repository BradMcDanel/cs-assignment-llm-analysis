# Your code for Milestone 4: Let the user try to find the words

from SpellingBeeGraphics import SpellingBeeGraphics

def user_word_action(word):
    puzzle = sbg.get_beehive_letters()
    words = read_dictionary(DICTIONARY_FILE)
    total_score = 0
    word_count = 0
    
    if word.lower() in words:
        if is_legal_word(word, puzzle):
            score = calculate_score(word)
            sbg.add_word(f"{word} ({score})")
            total_score += score
            word_count += 1
        else:
            sbg.show_message("Word does not meet puzzle criteria", "Red")
    else:
        sbg.show_message("Word not found in dictionary", "Red")
    
    sbg.show_message(f"Total words found: {word_count}, Total score: {total_score}")

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

# Startup code
sbg = SpellingBeeGraphics()
sbg.add_field("Puzzle", puzzle_action)
sbg.add_field("Word", user_word_action)
sbg.add_button("Solve", solve_action)