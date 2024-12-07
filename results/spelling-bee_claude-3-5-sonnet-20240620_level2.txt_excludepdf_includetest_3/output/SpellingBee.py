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

    def word_is_valid(word, puzzle):
        center = puzzle[0].lower()
        puzzle_set = set(puzzle.lower())
        return (len(word) >= 4 and
                center in word and
                set(word).issubset(puzzle_set))

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
            sbg.show_message("Puzzle set successfully!")
        else:
            sbg.show_message("Invalid puzzle. Please enter 7 unique letters.", "Red")

    def solve_action(s):
        puzzle = sbg.get_beehive_letters()
        if not puzzle:
            sbg.show_message("Please set a puzzle first.", "Red")
            return

        sbg.clear_word_list()
        words = read_dictionary()
        valid_words = [word for word in words if word_is_valid(word, puzzle)]
        
        total_score = 0
        word_count = 0
        for word in valid_words:
            score = calculate_score(word, puzzle)
            total_score += score
            word_count += 1
            color = "Blue" if set(word) == set(puzzle.lower()) else None
            sbg.add_word(f"{word} ({score})", color)

        sbg.show_message(f"Found {word_count} words. Total score: {total_score}")

    def word_action(s):
        puzzle = sbg.get_beehive_letters()
        if not puzzle:
            sbg.show_message("Please set a puzzle first.", "Red")
            return

        word = s.lower()
        if word in found_words:
            sbg.show_message("Word already found!", "Red")
        elif word not in dictionary:
            sbg.show_message("Word not in dictionary.", "Red")
        elif not word_is_valid(word, puzzle):
            if len(word) < 4:
                sbg.show_message("Word must be at least 4 letters long.", "Red")
            elif puzzle[0].lower() not in word:
                sbg.show_message("Word must contain the center letter.", "Red")
            else:
                sbg.show_message("Word contains invalid letters.", "Red")
        else:
            score = calculate_score(word, puzzle)
            color = "Blue" if set(word) == set(puzzle.lower()) else None
            sbg.add_word(f"{word} ({score})", color)
            found_words.add(word)
            total_score[0] += score
            word_count[0] += 1
            sbg.show_message(f"Found {word_count[0]} words. Total score: {total_score[0]}")
        
        sbg.set_field("Word", "")  # Clear the word field

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action, 7)
    sbg.add_button("Solve", solve_action)
    sbg.add_field("Word", word_action)

    dictionary = read_dictionary()
    found_words = set()
    total_score = [0]  # Using a list to make it mutable
    word_count = [0]  # Using a list to make it mutable

if __name__ == "__main__":
    spelling_bee()