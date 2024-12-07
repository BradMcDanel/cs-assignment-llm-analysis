from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

def spelling_bee():
    def puzzle_action(s):
        # Check if the puzzle string is valid
        if not is_valid_puzzle(s):
            sbg.show_message("Puzzle must be 7 unique letters.", "Red")
            return
        # Set the beehive letters
        sbg.set_beehive_letters(s.upper())
        sbg.show_message("Puzzle set!", "Green")

    def solve_action(s):
        # Clear previous words
        sbg.clear_word_list()
        # Load dictionary
        words = load_dictionary()
        # Get current puzzle letters from beehive
        beehive_letters = sbg.get_beehive_letters()
        center_letter = beehive_letters[0].lower()

        # Find valid words
        found_words = []
        total_score = 0

        for word in words:
            if is_valid_word(word, beehive_letters, center_letter):
                score = calculate_score(word, beehive_letters)
                if set(word) == set(beehive_letters.lower()):
                    sbg.add_word(word, "Blue")  # pangram in blue
                else:
                    sbg.add_word(word, "Black")
                found_words.append(word)
                total_score += score

        # Display results
        sbg.show_message(f"Found {len(found_words)} words with total score: {total_score}", "Green")

    def is_valid_puzzle(puzzle):
        # Check if the puzzle string has exactly 7 unique letters
        return len(puzzle) == 7 and len(set(puzzle)) == 7 and puzzle.isalpha()

    def load_dictionary():
        # Load the dictionary from the provided file
        with open(DICTIONARY_FILE, 'r') as file:
            return [line.strip() for line in file]

    def is_valid_word(word, beehive_letters, center_letter):
        # Check word length and if it contains the center letter
        if len(word) < 4 or center_letter not in word:
            return False
        # Check if word contains only letters from the beehive
        return all(char in beehive_letters.lower() for char in word)

    def calculate_score(word, beehive_letters):
        # Calculate score based on word length and if it's a pangram
        score = len(word) if len(word) > 4 else 1
        if set(word) == set(beehive_letters.lower()):
            score += 7  # Pangram bonus
        return score

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

if __name__ == "__main__":
    spelling_bee()