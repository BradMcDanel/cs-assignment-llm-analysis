from SpellingBeeGraphics import SpellingBeeGraphics

def calculate_score(word):
    pangram_bonus = 7 if len(set(word)) == 7 else 0
    return len(word) + pangram_bonus

def solve_action(s):
    puzzle = sbg.get_beehive_letters()
    dictionary = load_dictionary(DICTIONARY_FILE)
    total_score = 0
    word_count = 0

    for word in dictionary:
        if check_word(word, puzzle):
            score = calculate_score(word)
            sbg.add_word(f"{word} ({score})")
            total_score += score
            word_count += 1

    sbg.show_message(f"Total Words Found: {word_count}, Total Score: {total_score}")

sbg = SpellingBeeGraphics()
sbg.add_field("Puzzle", lambda s: sbg.set_beehive_letters(s.upper()))
sbg.add_button("Solve", solve_action)