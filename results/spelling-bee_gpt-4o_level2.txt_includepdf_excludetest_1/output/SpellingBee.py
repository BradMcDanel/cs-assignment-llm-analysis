from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

def spelling_bee():

    found_words = set()

    def is_legal_puzzle(puzzle):
        return len(puzzle) == 7 and all(c.isalpha() for c in puzzle) and len(set(puzzle)) == 7

    def puzzle_action(puzzle):
        puzzle = puzzle.upper()
        if is_legal_puzzle(puzzle):
            sbg.set_beehive_letters(puzzle)
            sbg.show_message("Puzzle set successfully", "Green")
            found_words.clear()  # Reset found words for new puzzle
        else:
            sbg.show_message("Invalid Puzzle: Must be 7 unique letters", "Red")

    def load_dictionary():
        with open(DICTIONARY_FILE, 'r') as file:
            return set(word.strip().lower() for word in file)

    def is_valid_word(word, beehive_letters, center_letter):
        return (
            len(word) >= 4 and
            all(c in beehive_letters for c in word) and
            center_letter in word
        )

    def calculate_score(word, beehive_letters):
        score = len(word) if len(word) == 4 else len(word)
        if all(c in word for c in beehive_letters):
            score += 7  # Pangram bonus
        return score

    def solve_action(s):
        sbg.clear_word_list()
        beehive_letters = sbg.get_beehive_letters().lower()
        center_letter = beehive_letters[0]
        dictionary = load_dictionary()
        total_score = 0
        word_count = 0
        for word in dictionary:
            if is_valid_word(word, beehive_letters, center_letter):
                score = calculate_score(word, beehive_letters)
                sbg.add_word(f"{word} ({score})", color="Blue" if score > len(word) else "Black")
                total_score += score
                word_count += 1
        sbg.show_message(f"Found {word_count} words with total score {total_score}", "Green")

    def word_action(word):
        word = word.lower()
        beehive_letters = sbg.get_beehive_letters().lower()
        center_letter = beehive_letters[0]
        dictionary = load_dictionary()
        if word in found_words:
            sbg.show_message("Word already found!", "Red")
        elif word not in dictionary:
            sbg.show_message("Word not in dictionary!", "Red")
        elif not is_valid_word(word, beehive_letters, center_letter):
            sbg.show_message("Word does not meet puzzle rules!", "Red")
        else:
            found_words.add(word)
            score = calculate_score(word, beehive_letters)
            sbg.add_word(f"{word} ({score})", color="Blue" if score > len(word) else "Black")
            sbg.show_message(f"Word '{word}' added with score {score}", "Green")
            sbg.set_field("Word", "")  # Clear the input field

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)
    sbg.add_field("Word", word_action)

if __name__ == "__main__":
    spelling_bee()