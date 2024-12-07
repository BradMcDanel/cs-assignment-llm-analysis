from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

def spelling_bee():
    def is_valid_puzzle(puzzle):
        return (len(puzzle) == 7 and
                puzzle.isalpha() and
                len(set(puzzle)) == 7)

    def puzzle_action(s):
        puzzle = s.upper()
        if is_valid_puzzle(puzzle):
            sbg.set_beehive_letters(puzzle)
            sbg.show_message("Puzzle set successfully!", "Green")
        else:
            sbg.show_message("Invalid puzzle. Please enter 7 unique letters.", "Red")

    def read_dictionary():
        with open(DICTIONARY_FILE, 'r') as f:
            return set(word.strip().lower() for word in f)

    def is_valid_word(word, puzzle):
        center = puzzle[0].lower()
        puzzle_set = set(puzzle.lower())
        return (len(word) >= 4 and
                center in word and
                all(letter in puzzle_set for letter in word))

    def calculate_score(word, puzzle):
        score = len(word)
        if score == 4:
            score = 1
        if set(word) == set(puzzle.lower()):
            score += 7  # Pangram bonus
        return score

    def solve_action(s):
        puzzle = sbg.get_beehive_letters()
        if not puzzle:
            sbg.show_message("Please set a valid puzzle first.", "Red")
            return

        dictionary = read_dictionary()
        valid_words = []
        total_score = 0
        pangrams = []

        for word in dictionary:
            if is_valid_word(word, puzzle):
                score = calculate_score(word, puzzle)
                valid_words.append((word, score))
                total_score += score
                if set(word) == set(puzzle.lower()):
                    pangrams.append(word)

        sbg.clear_word_list()
        for word, score in sorted(valid_words):
            color = "Blue" if word in pangrams else "Black"
            sbg.add_word(f"{word} ({score})", color)

        message = f"Found {len(valid_words)} words. Total score: {total_score}"
        sbg.show_message(message, "Green")

    def word_action(s):
        puzzle = sbg.get_beehive_letters()
        if not puzzle:
            sbg.show_message("Please set a valid puzzle first.", "Red")
            return

        word = s.lower()
        dictionary = read_dictionary()

        if word not in dictionary:
            sbg.show_message("Word not in dictionary.", "Red")
        elif not is_valid_word(word, puzzle):
            if len(word) < 4:
                sbg.show_message("Word must be at least 4 letters long.", "Red")
            elif puzzle[0].lower() not in word:
                sbg.show_message("Word must contain the center letter.", "Red")
            else:
                sbg.show_message("Word contains invalid letters.", "Red")
        else:
            score = calculate_score(word, puzzle)
            color = "Blue" if set(word) == set(puzzle.lower()) else "Black"
            sbg.add_word(f"{word} ({score})", color)
            sbg.set_field("Word", "")  # Clear the word field
            current_message = sbg.get_field("Message")
            if current_message:
                total_words, total_score = map(int, current_message.split()[-4::2])
                total_words += 1
                total_score += score
            else:
                total_words, total_score = 1, score
            sbg.show_message(f"Found {total_words} words. Total score: {total_score}", "Green")

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action, 7)
    sbg.add_field("Word", word_action)
    sbg.add_button("Solve", solve_action)

# Startup code
if __name__ == "__main__":
    spelling_bee()