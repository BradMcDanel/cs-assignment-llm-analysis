from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

# Utility function to read dictionary file
def read_dictionary(file_path):
    with open(file_path, 'r') as file:
        return [line.strip().lower() for line in file]

# Utility function to check if puzzle is legal
def is_legal_puzzle(puzzle):
    if len(puzzle) != 7:
        return "Puzzle must contain exactly seven characters."
    if not puzzle.isalpha():
        return "Puzzle must contain only alphabetic characters."
    if len(set(puzzle)) != 7:
        return "Puzzle must not contain duplicate characters."
    return None

# Utility function to check if word is valid
def is_valid_word(word, puzzle, center_letter):
    if len(word) < 4:
        return False
    if center_letter not in word:
        return False
    for char in word:
        if char not in puzzle:
            return False
    return True

# Main function
def spelling_bee():
    dictionary = read_dictionary(DICTIONARY_FILE)

    def puzzle_action(puzzle):
        puzzle = puzzle.upper()
        validation_message = is_legal_puzzle(puzzle)
        if validation_message:
            sbg.show_message(validation_message, "Red")
        else:
            sbg.set_beehive_letters(puzzle)
            sbg.show_message("Puzzle set successfully!", "Green")

    def solve_action(button_name):
        puzzle = sbg.get_beehive_letters().lower()
        center_letter = puzzle[0]
        sbg.clear_word_list()
        total_score = 0
        found_words = []
        for word in dictionary:
            if is_valid_word(word, puzzle, center_letter):
                score = len(word) + (7 if len(set(word)) == 7 else 0)
                total_score += score
                color = "Blue" if score > len(word) else "Black"
                sbg.add_word(f"{word} ({score})", color)
                found_words.append(word)
        sbg.show_message(f"Total Score: {total_score}, Words Found: {len(found_words)}", "Green")

    def word_action(user_word):
        user_word = user_word.lower()
        puzzle = sbg.get_beehive_letters().lower()
        center_letter = puzzle[0]
        if user_word in dictionary and is_valid_word(user_word, puzzle, center_letter):
            score = len(user_word) + (7 if len(set(user_word)) == 7 else 0)
            sbg.add_word(f"{user_word} ({score})", "Blue" if len(set(user_word)) == 7 else "Black")
            sbg.show_message(f"Word accepted! Score: {score}", "Green")
        else:
            sbg.show_message("Word not valid or already found.", "Red")
        sbg.set_field("Word", "")

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)
    sbg.add_field("Word", word_action)

# Startup code
if __name__ == "__main__":
    spelling_bee()