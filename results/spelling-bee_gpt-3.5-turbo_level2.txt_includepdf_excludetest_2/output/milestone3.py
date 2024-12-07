from SpellingBeeGraphics import SpellingBeeGraphics

def calculate_score(word):
    score = len(word)
    if len(word) == 7:
        score += 7  # Bonus for pangram
    return score

def solve_action(s):
    puzzle = sbg.get_beehive_letters()
    dictionary = read_dictionary(DICTIONARY_FILE)
    
    total_score = 0
    word_count = 0
    
    for word in dictionary:
        if is_valid_word(word, puzzle):
            score = calculate_score(word)
            sbg.add_word(f"{word} ({score})")
            total_score += score
            word_count += 1
    
    sbg.show_message(f"Words found: {word_count}, Total Score: {total_score}")

sbg = SpellingBeeGraphics()
sbg.add_field("Puzzle", lambda s: None)
sbg.add_button("Solve", solve_action)