from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

# Helper function to read the dictionary file
def read_dictionary(file_path):
    with open(file_path, 'r') as file:
        words = [line.strip().lower() for line in file]
    return words

# Helper function to check if the puzzle string is valid
def is_valid_puzzle(puzzle):
    if len(puzzle) != 7:
        return "Puzzle must contain exactly seven characters."
    if not puzzle.isalpha():
        return "Puzzle must only contain alphabetic characters."
    if len(set(puzzle)) != 7:
        return "Puzzle cannot contain duplicate letters."
    return None

# Helper function to check if a word is valid for the puzzle
def is_valid_word(word, puzzle, center_letter):
    if len(word) < 4:
        return False
    if center_letter not in word:
        return False
    if any(char not in puzzle for char in word):
        return False
    return True

# Spelling Bee main function
def spelling_bee():
    # Load the dictionary
    dictionary = read_dictionary(DICTIONARY_FILE)

    def puzzle_action(puzzle):
        puzzle = puzzle.upper()
        error_message = is_valid_puzzle(puzzle)
        if error_message:
            sbg.show_message(error_message, "Red")
        else:
            sbg.set_beehive_letters(puzzle)
            sbg.show_message("Puzzle is set!", "Green")

    def solve_action(s):
        puzzle = sbg.get_beehive_letters().lower()
        if not puzzle:
            sbg.show_message("No puzzle set!", "Red")
            return
        
        center_letter = puzzle[0]
        valid_words = [word for word in dictionary if is_valid_word(word, puzzle, center_letter)]
        
        sbg.clear_word_list()
        total_score = 0
        for word in valid_words:
            score = len(word) if len(word) > 4 else 1
            if set(word) == set(puzzle):
                score += 7
                sbg.add_word(word, "Blue")
            else:
                sbg.add_word(word, "Black")
            total_score += score
        
        sbg.show_message(f'Found {len(valid_words)} words with total score {total_score}', "Green")

    def word_action(word):
        puzzle = sbg.get_beehive_letters().lower()
        if not puzzle:
            sbg.show_message("No puzzle set!", "Red")
            return
        
        center_letter = puzzle[0]
        word = word.lower()
        
        if word not in dictionary:
            sbg.show_message("Word not in dictionary.", "Red")
        elif not is_valid_word(word, puzzle, center_letter):
            sbg.show_message("Invalid word for this puzzle.", "Red")
        else:
            score = len(word) if len(word) > 4 else 1
            if set(word) == set(puzzle):
                score += 7
                sbg.add_word(word, "Blue")
            else:
                sbg.add_word(word, "Black")
            sbg.show_message(f"Word accepted with score {score}.", "Green")
            sbg.set_field("Word", "")

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_field("Word", word_action)
    sbg.add_button("Solve", solve_action)

# Startup code
if __name__ == "__main__":
    spelling_bee()