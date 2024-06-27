from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

def spelling_bee():
    def is_legal_puzzle(puzzle):
        if len(puzzle) != 7:
            return False, "Puzzle must contain exactly seven characters."
        if not all(char.isalpha() for char in puzzle):
            return False, "Puzzle must contain only letters."
        if len(set(puzzle)) != 7:
            return False, "Puzzle must not contain duplicate letters."
        return True, ""

    def puzzle_action(puzzle):
        puzzle = puzzle.upper()
        is_legal, message = is_legal_puzzle(puzzle)
        if is_legal:
            sbg.set_beehive_letters(puzzle)
            sbg.show_message("Puzzle updated successfully.", "Green")
        else:
            sbg.show_message(message, "Red")

    def load_dictionary():
        with open(DICTIONARY_FILE) as f:
            return set(word.strip().lower() for word in f)

    def is_valid_word(word, letters, center_letter):
        if len(word) < 4:
            return False
        if center_letter not in word:
            return False
        if any(char not in letters for char in word):
            return False
        return True

    def solve_action(name):
        sbg.clear_word_list()
        letters = sbg.get_beehive_letters().lower()
        center_letter = letters[0]
        dictionary = load_dictionary()
        found_words = []
        total_score = 0

        for word in dictionary:
            if is_valid_word(word, letters, center_letter):
                score = 1 if len(word) == 4 else len(word)
                if set(word) == set(letters):
                    score += 7
                    sbg.add_word(f"{word} ({score})", "Blue")
                else:
                    sbg.add_word(f"{word} ({score})")
                found_words.append(word)
                total_score += score

        sbg.show_message(f"Found {len(found_words)} words, Total score: {total_score}", "Blue")

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

if __name__ == "__main__":
    spelling_bee()