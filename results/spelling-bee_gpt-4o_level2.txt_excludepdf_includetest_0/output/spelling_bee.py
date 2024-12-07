from SpellingBeeGraphics import SpellingBeeGraphics

DICTIONARY_FILE = "EnglishWords.txt"

def spelling_bee():
    found_words = set()

    def puzzle_action(puzzle_input):
        if is_legal_puzzle(puzzle_input):
            sbg.set_beehive_letters(puzzle_input.upper())
            sbg.show_message("Puzzle set successfully.", "Green")
        else:
            sbg.show_message("Invalid puzzle. Ensure 7 unique letters.", "Red")

    def solve_action(s):
        puzzle = sbg.get_beehive_letters().lower()
        center_letter = puzzle[0]
        valid_words = find_valid_words(puzzle, center_letter)
        sbg.clear_word_list()
        total_score = 0
        for word in valid_words:
            score = calculate_word_score(word, puzzle)
            total_score += score
            color = "Blue" if is_pangram(word, puzzle) else "Black"
            sbg.add_word(f"{word} ({score})", color)
        sbg.show_message(f"Total Words: {len(valid_words)}, Total Score: {total_score}", "Green")

    def word_action(word_input):
        word_input = word_input.lower()
        puzzle = sbg.get_beehive_letters().lower()
        center_letter = puzzle[0]
        if word_input in found_words:
            sbg.show_message("Word already found.", "Red")
        elif word_input not in load_dictionary():
            sbg.show_message("Word not in dictionary.", "Red")
        elif len(word_input) < 4:
            sbg.show_message("Word too short.", "Red")
        elif any(ch not in puzzle for ch in word_input):
            sbg.show_message("Word contains invalid letters.", "Red")
        elif center_letter not in word_input:
            sbg.show_message("Word does not contain center letter.", "Red")
        else:
            found_words.add(word_input)
            score = calculate_word_score(word_input, puzzle)
            color = "Blue" if is_pangram(word_input, puzzle) else "Black"
            sbg.add_word(f"{word_input} ({score})", color)
            sbg.show_message(f"Words Found: {len(found_words)}, Total Score: {sum(calculate_word_score(word, puzzle) for word in found_words)}", "Green")
            sbg.set_field("Word", "")

    def is_legal_puzzle(puzzle):
        if len(puzzle) != 7:
            return False
        if not puzzle.isalpha():
            return False
        if len(set(puzzle)) != 7:
            return False
        return True

    def load_dictionary():
        with open(DICTIONARY_FILE, 'r') as f:
            return set(word.strip().lower() for word in f)

    def find_valid_words(puzzle, center):
        valid_words = []
        dictionary = load_dictionary()
        for word in dictionary:
            if len(word) >= 4 and all(ch in puzzle for ch in word) and center in word:
                valid_words.append(word)
        return valid_words

    def calculate_word_score(word, puzzle):
        score = len(word) if len(word) > 4 else 1
        if is_pangram(word, puzzle):
            score += 7
        return score

    def is_pangram(word, puzzle):
        return all(ch in word for ch in puzzle)

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)
    sbg.add_field("Word", word_action)

if __name__ == "__main__":
    spelling_bee()