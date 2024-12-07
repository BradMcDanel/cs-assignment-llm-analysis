from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

def spelling_bee():
    def read_dictionary():
        with open(DICTIONARY_FILE, 'r') as file:
            return set(word.strip().lower() for word in file)

    def is_valid_puzzle(puzzle):
        return (len(puzzle) == 7 and
                puzzle.isalpha() and
                len(set(puzzle)) == 7)

    def word_is_valid(word, puzzle):
        center_letter = puzzle[0].lower()
        puzzle_set = set(puzzle.lower())
        return (len(word) >= 4 and
                set(word).issubset(puzzle_set) and
                center_letter in word)

    def calculate_score(word):
        if len(word) == 4:
            return 1
        elif len(set(word)) == 7:
            return len(word) + 7
        else:
            return len(word)

    def puzzle_action(s):
        if is_valid_puzzle(s):
            sbg.set_beehive_letters(s.upper())
            sbg.show_message("Puzzle set successfully!")
        else:
            sbg.show_message("Invalid puzzle. Please enter 7 unique letters.", "Red")

    def solve_action(s):
        puzzle = sbg.get_beehive_letters()
        if not puzzle:
            sbg.show_message("Please set a valid puzzle first.", "Red")
            return

        sbg.clear_word_list()
        words = read_dictionary()
        valid_words = []
        total_score = 0
        for word in words:
            if word_is_valid(word, puzzle):
                score = calculate_score(word)
                total_score += score
                valid_words.append((word, score))

        for word, score in sorted(valid_words):
            color = "Blue" if len(set(word)) == 7 else "Black"
            sbg.add_word(f"{word} ({score})", color)

        message = f"Found {len(valid_words)} words. Total score: {total_score}"
        sbg.show_message(message)

    def word_action(s):
        puzzle = sbg.get_beehive_letters()
        if not puzzle:
            sbg.show_message("Please set a valid puzzle first.", "Red")
            return

        word = s.lower()
        if not word_is_valid(word, puzzle):
            if len(word) < 4:
                sbg.show_message("Word must be at least 4 letters long.", "Red")
            elif puzzle[0].lower() not in word:
                sbg.show_message("Word must contain the center letter.", "Red")
            elif not set(word).issubset(set(puzzle.lower())):
                sbg.show_message("Word contains letters not in the puzzle.", "Red")
            else:
                sbg.show_message("Invalid word.", "Red")
        else:
            words = read_dictionary()
            if word not in words:
                sbg.show_message("Word is not in the dictionary.", "Red")
            else:
                score = calculate_score(word)
                color = "Blue" if len(set(word)) == 7 else "Black"
                sbg.add_word(f"{word} ({score})", color)
                sbg.show_message(f"Valid word! Score: {score}")
        
        sbg.set_field("Word", "")  # Clear the word field

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)
    sbg.add_field("Word", word_action)

# Startup code
if __name__ == "__main__":
    spelling_bee()