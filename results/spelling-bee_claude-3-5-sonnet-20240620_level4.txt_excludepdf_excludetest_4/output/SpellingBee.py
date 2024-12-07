from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

def spelling_bee():
    def read_dictionary():
        with open(DICTIONARY_FILE, 'r') as f:
            return set(word.strip().lower() for word in f)

    def is_valid_puzzle(puzzle):
        return (len(puzzle) == 7 and
                puzzle.isalpha() and
                len(set(puzzle)) == 7)

    def is_valid_word(word, puzzle):
        center = puzzle[0].lower()
        puzzle_set = set(puzzle.lower())
        return (len(word) >= 4 and
                set(word).issubset(puzzle_set) and
                center in word)

    def calculate_score(word, puzzle):
        score = len(word)
        if score == 4:
            score = 1
        if set(word) == set(puzzle.lower()):
            score += 7  # Pangram bonus
        return score

    def puzzle_action(s):
        puzzle = s.upper()
        if is_valid_puzzle(puzzle):
            sbg.set_beehive_letters(puzzle)
            sbg.show_message("Puzzle set successfully!", "Green")
        else:
            sbg.show_message("Invalid puzzle. Please enter 7 unique letters.", "Red")

    def solve_action(s):
        puzzle = sbg.get_beehive_letters()
        if not puzzle:
            sbg.show_message("Please set a puzzle first.", "Red")
            return

        sbg.clear_word_list()
        words = read_dictionary()
        valid_words = []
        total_score = 0
        for word in words:
            if is_valid_word(word, puzzle):
                score = calculate_score(word, puzzle)
                valid_words.append((word, score))
                total_score += score

        for word, score in sorted(valid_words):
            color = "Blue" if set(word) == set(puzzle.lower()) else "Black"
            sbg.add_word(f"{word} ({score})", color)

        message = f"Found {len(valid_words)} words. Total score: {total_score}"
        sbg.show_message(message, "Green")

    def word_action(s):
        puzzle = sbg.get_beehive_letters()
        if not puzzle:
            sbg.show_message("Please set a puzzle first.", "Red")
            return

        word = s.lower()
        if not is_valid_word(word, puzzle):
            if len(word) < 4:
                sbg.show_message("Word must be at least 4 letters long.", "Red")
            elif puzzle[0].lower() not in word:
                sbg.show_message("Word must contain the center letter.", "Red")
            elif not set(word).issubset(set(puzzle.lower())):
                sbg.show_message("Word contains invalid letters.", "Red")
            else:
                sbg.show_message("Not a valid word in the dictionary.", "Red")
        else:
            score = calculate_score(word, puzzle)
            color = "Blue" if set(word) == set(puzzle.lower()) else "Black"
            sbg.add_word(f"{word} ({score})", color)
            sbg.set_field("Word", "")  # Clear the word field
            
            # Update total score and word count
            current_message = sbg.get_field("Message")
            if "Found" in current_message:
                words, total_score = map(int, current_message.split()[1::2])
                words += 1
                total_score += score
                message = f"Found {words} words. Total score: {total_score}"
                sbg.show_message(message, "Green")
            else:
                sbg.show_message(f"Found 1 word. Total score: {score}", "Green")

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action, 7)
    sbg.add_field("Word", word_action)
    sbg.add_button("Solve", solve_action)

# Startup code
if __name__ == "__main__":
    spelling_bee()