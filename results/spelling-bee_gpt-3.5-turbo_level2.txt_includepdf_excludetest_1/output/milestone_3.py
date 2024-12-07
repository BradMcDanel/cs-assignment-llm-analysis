from SpellingBeeGraphics import SpellingBeeGraphics

def solve_action(s):
    puzzle = sbg.get_beehive_letters()
    dictionary = read_dictionary(DICTIONARY_FILE)
    
    total_score = 0
    words_found = 0
    
    for word in dictionary:
        if is_valid_word(word, puzzle):
            score = calculate_score(word)
            sbg.add_word(f"{word} ({score})")
            total_score += score
            words_found += 1
    
    sbg.show_message(f"Words found: {words_found}, Total Score: {total_score}")

# Function to calculate score of a word
def calculate_score(word):
    if len(word) == 4:
        return 1
    elif len(word) > 4:
        return len(word)
    else:
        return 0

# Main program
sbg = SpellingBeeGraphics()
sbg.add_field("Puzzle", puzzle_action)
sbg.add_button("Solve", solve_action)