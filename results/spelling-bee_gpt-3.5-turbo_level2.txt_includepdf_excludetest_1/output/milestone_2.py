from SpellingBeeGraphics import SpellingBeeGraphics

def solve_action(s):
    puzzle = sbg.get_beehive_letters()
    dictionary = read_dictionary(DICTIONARY_FILE)
    
    for word in dictionary:
        if is_valid_word(word, puzzle):
            sbg.add_word(word)
            
# Function to read dictionary into a list
def read_dictionary(file):
    with open(file, 'r') as f:
        return [line.strip() for line in f]

# Function to check if word is valid
def is_valid_word(word, puzzle):
    if len(word) < 4:
        return False
    
    if not all(char in puzzle for char in word):
        return False
    
    if puzzle[0] not in word:
        return False
    
    return True

# Main program
sbg = SpellingBeeGraphics()
sbg.add_field("Puzzle", puzzle_action)
sbg.add_button("Solve", solve_action)