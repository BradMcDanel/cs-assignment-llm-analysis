from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

def spelling_bee():
    def read_dictionary():
        with open(DICTIONARY_FILE, "r") as file:
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

    def calculate_score(word):
        base_score = max(1, len(word))
        pangram_bonus = 7 if len(set(word)) == 7 else 0
        return base_score + pangram_bonus

    def find_words(puzzle, dictionary):
        return [word for word in dictionary if is_valid_word(word, puzzle)]

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
            sbg.show_message("Please set a valid puzzle first.", "Red")
            return

        dictionary = read_dictionary()
        valid_words = find_words(puzzle, dictionary)
        
        sbg.clear_word_list()
        total_score = 0
        for word in valid_words:
            score = calculate_score(word)
            total_score += score
            color = "Blue" if len(set(word)) == 7 else "Black"
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
            score = calculate_score(word)
            color = "Blue" if len(set(word)) == 7 else "Black"
            sbg.add_word(f"{word} ({score})", color)
            sbg.set_field("Word", "")
            
            current_words = [w.split()[0] for w in sbg.get_word_list()]
            total_score = sum(calculate_score(w) for w in current_words)
            message = f"Found {len(current_words)} words. Total score: {total_score}"
            sbg.show_message(message, "Green")

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action, 7)
    sbg.add_field("Word", word_action)
    sbg.add_button("Solve", solve_action)

# Startup code
if __name__ == "__main__":
    spelling_bee()