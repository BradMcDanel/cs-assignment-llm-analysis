from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

# Read dictionary from file into a list
def read_dictionary():
    with open(DICTIONARY_FILE, 'r') as file:
        dictionary = [line.strip().lower() for line in file]
    return dictionary

# Check if a word meets the requirements
def is_valid_word(word, beehive):
    if len(word) < 4:
        return False
    if set(word) - set(beehive):
        return False
    if beehive[0] not in word:
        return False
    return True

# Check each word in the dictionary against the beehive
def check_words(dictionary, beehive, sbg):
    words_found = 0
    total_score = 0
    for word in dictionary:
        if is_valid_word(word, beehive):
            words_found += 1
            word_score = len(word) + (7 if len(word) == 7 else 0)
            total_score += word_score
            sbg.add_word(word, "Blue" if len(word) == 7 else "Black")
    sbg.show_message(f"Words found: {words_found}, Total Score: {total_score}")
    
# Main function for Spelling Bee
def spelling_bee():
    sbg = SpellingBeeGraphics()
    dictionary = read_dictionary()
    
    def puzzle_action(s):
        puzzle = sbg.get_field("Puzzle").upper()
        if len(puzzle) != 7 or not all(char.isalpha() for char in puzzle) or len(set(puzzle)) != 7:
            sbg.show_message("Invalid puzzle, must be 7 unique letters.", "Red")
        else:
            sbg.set_beehive_letters(puzzle)
            sbg.show_message("", "Black")
    
    def solve_action(s):
        beehive = sbg.get_beehive_letters()
        check_words(dictionary, beehive, sbg)
    
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

if __name__ == "__main__":
    spelling_bee()