from SpellingBeeGraphics import SpellingBeeGraphics

DICTIONARY_FILE = "EnglishWords.txt"

def spelling_bee():
    def puzzle_action(s):
        puzzle = sbg.get_field("Puzzle")
        if validate_puzzle(puzzle):
            sbg.set_beehive_letters(puzzle)
        else:
            sbg.show_message("Invalid puzzle. Must be 7 unique letters from A-Z.", "Red")

    def solve_action(s):
        puzzle = sbg.get_beehive_letters()
        dictionary = read_dictionary(DICTIONARY_FILE)
        for word in dictionary:
            if validate_word(word, puzzle):
                sbg.add_word(word)
        calculate_score()

    def validate_puzzle(puzzle):
        if len(puzzle) != 7:
            return False
        if len(set(puzzle)) != 7:
            return False
        if any(letter not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for letter in puzzle):
            return False
        return True

    def read_dictionary(filename):
        with open(filename, "r") as file:
            return [line.strip() for line in file]

    def validate_word(word, puzzle):
        if len(word) < 4:
            return False
        if len(set(word) - set(puzzle)) > 0:
            return False
        if puzzle[0] not in word:
            return False
        return True

    def calculate_score():
        words = sbg.words
        total_score = 0
        pangram_count = 0
        for word, _ in words:
            score = len(word)
            if len(word) == 7:
                score += 7
                pangram_count += 1
            sbg.add_word(f"{word} ({score})")
            total_score += score
        sbg.show_message(f"Found {len(words)} words with a total score of {total_score} and {pangram_count} pangrams.", "Green")

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

if __name__ == "__main__":
    spelling_bee()