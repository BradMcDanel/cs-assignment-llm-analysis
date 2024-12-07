from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

def read_dictionary():
    """Reads the dictionary file and returns a set of valid words."""
    with open(DICTIONARY_FILE, 'r') as file:
        return set(word.strip().lower() for word in file)

def is_valid_puzzle(puzzle):
    """Check if the puzzle is valid according to the rules."""
    return (
        len(puzzle) == 7 and
        puzzle.isalpha() and
        len(set(puzzle)) == 7
    )

def puzzle_action(s):
    """Handles the action when the puzzle is updated."""
    if is_valid_puzzle(s):
        sbg.set_beehive_letters(s)
        sbg.show_message("Puzzle set successfully!", "Green")
    else:
        sbg.show_message("Invalid puzzle: must be 7 unique letters.", "Red")

def is_valid_word(word, center_letter, beehive_letters):
    """Check if the word is valid according to the rules."""
    return (
        len(word) >= 4 and
        center_letter in word and
        all(c in beehive_letters for c in word)
    )

def solve_action(s):
    """Handles the action when the Solve button is clicked."""
    beehive_letters = sbg.get_beehive_letters().lower()
    center_letter = beehive_letters[0]
    valid_words = []
    total_score = 0

    for word in dictionary:
        if is_valid_word(word, center_letter, beehive_letters):
            score = len(word) if len(word) > 4 else 1
            if set(word) == set(beehive_letters):
                score += 7  # Pangram bonus
                sbg.add_word(f"{word} ({score})", "Blue")
            else:
                sbg.add_word(f"{word} ({score})")
            valid_words.append(word)
            total_score += score
    
    sbg.show_message(f"Total words: {len(valid_words)}, Total score: {total_score}", "Black")

# Main function
def spelling_bee():
    global sbg, dictionary
    sbg = SpellingBeeGraphics()
    dictionary = read_dictionary()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

# Startup code
if __name__ == "__main__":
    spelling_bee()