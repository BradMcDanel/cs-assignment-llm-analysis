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
            score += 7
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
        valid_words = [word for word in words if is_valid_word(word, puzzle)]
        
        total_score = 0
        word_count = 0
        for word in valid_words:
            score = calculate_score(word, puzzle)
            total_score += score
            word_count += 1
            color = "Blue" if set(word) == set(puzzle.lower()) else "Black"
            sbg.add_word(f"{word} ({score})", color)

        sbg.show_message(f"Found {word_count} words. Total score: {total_score}", "Green")

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
                sbg.show_message("Word contains letters not in the puzzle.", "Red")
            else:
                sbg.show_message("Not a valid word.", "Red")
        else:
            words = [w.split()[0] for w in sbg.get_word_list()]
            if word in words:
                sbg.show_message("Word already found.", "Red")
            else:
                score = calculate_score(word, puzzle)
                color = "Blue" if set(word) == set(puzzle.lower()) else "Black"
                sbg.add_word(f"{word} ({score})", color)
                sbg.set_field("Word", "")
                
                words.append(word)
                total_score = sum(calculate_score(w, puzzle) for w in words)
                sbg.show_message(f"Found {len(words)} words. Total score: {total_score}", "Green")

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action, 7)
    sbg.add_field("Word", word_action)
    sbg.add_button("Solve", solve_action)

# Startup code
if __name__ == "__main__":
    spelling_bee()