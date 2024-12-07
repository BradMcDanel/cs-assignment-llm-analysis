from SpellingBeeGraphics import SpellingBeeGraphics

def puzzle_action(s):
    # Same as Milestone 1

def solve_action(s):
    # Same as Milestone 2

def word_action(word):
    puzzle = sbg.get_beehive_letters()
    dictionary = read_dictionary(DICTIONARY_FILE)
    
    if word.lower() not in dictionary:
        sbg.show_message("Word not in dictionary", "Red")
        return
    
    if not all(char in puzzle for char in word):
        sbg.show_message("Word contains letters not in the puzzle", "Red")
        return
    
    if len(word) < 4:
        sbg.show_message("Word must be at least four letters long", "Red")
        return
    
    if puzzle[0] not in word:
        sbg.show_message("Word must contain the center letter", "Red")
        return
    
    if word in sbg.get_word_list():
        sbg.show_message("Word already found", "Red")
        return
    
    score = calculate_score(word)
    sbg.add_word(f"{word} ({score})")
    sbg.show_message(f"Words found: {sbg.get_word_count()}, Total Score: {sbg.get_total_score()}")

# Main program
sbg = SpellingBeeGraphics()
sbg.add_field("Puzzle", puzzle_action)
sbg.add_button("Solve", solve_action)
sbg.add_field("Word", word_action)