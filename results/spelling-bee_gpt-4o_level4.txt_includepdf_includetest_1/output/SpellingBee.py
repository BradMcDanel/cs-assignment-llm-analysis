from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

def spelling_bee():
    def puzzle_action(s):
        if is_legal_puzzle(s):
            sbg.set_beehive_letters(s.upper())
            sbg.show_message("Puzzle set successfully.", "Green")
        else:
            sbg.show_message("Invalid puzzle: must be 7 unique letters.", "Red")

    def is_legal_puzzle(puzzle):
        if len(puzzle) != 7:
            return False
        unique_letters = set(puzzle.lower())
        return len(unique_letters) == 7 and all(c.isalpha() for c in puzzle)

    def solve_action(s):
        sbg.clear_word_list()
        beehive_letters = sbg.get_beehive_letters().lower()
        center_letter = beehive_letters[0]
        valid_words, total_score = find_valid_words(beehive_letters, center_letter)
        for word, score, is_pangram in valid_words:
            color = "Blue" if is_pangram else "Black"
            sbg.add_word(f"{word} ({score})", color)
        sbg.show_message(f"Found {len(valid_words)} words, Total score: {total_score}", "Black")

    def find_valid_words(beehive_letters, center_letter):
        with open(DICTIONARY_FILE, "r") as f:
            dictionary_words = f.read().splitlines()
        valid_words = []
        total_score = 0
        for word in dictionary_words:
            if is_valid_word(word, beehive_letters, center_letter):
                score = len(word) if len(word) > 4 else 1
                is_pangram = all(letter in word for letter in beehive_letters)
                if is_pangram:
                    score += 7
                valid_words.append((word, score, is_pangram))
                total_score += score
        return valid_words, total_score

    def is_valid_word(word, beehive_letters, center_letter):
        if len(word) < 4:
            return False
        if center_letter not in word:
            return False
        return all(c in beehive_letters for c in word)

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

# Startup code
if __name__ == "__main__":
    spelling_bee()