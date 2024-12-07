from SpellingBeeGraphics import SpellingBeeGraphics

DICTIONARY_FILE = "EnglishWords.txt"

def spelling_bee():
    def puzzle_action(s):
        puzzle = sbg.get_field("Puzzle")
        if is_legal_puzzle(puzzle):
            sbg.set_beehive_letters(puzzle)
        else:
            sbg.show_message("Invalid puzzle. Must contain exactly seven unique letters from A-Z.", "Red")

    def solve_action(s):
        puzzle = sbg.get_beehive_letters()
        dictionary = read_dictionary(DICTIONARY_FILE)
        words = find_legal_words(puzzle, dictionary)
        display_words(words)

    def is_legal_puzzle(puzzle):
        if len(puzzle) != 7:
            return False
        if len(set(puzzle)) != 7:
            return False
        return all('A' <= c <= 'Z' for c in puzzle)

    def read_dictionary(file):
        with open(file, 'r') as f:
            return set(word.strip() for word in f)

    def find_legal_words(puzzle, dictionary):
        center = puzzle[0]
        return [word for word in dictionary if len(word) >= 4 and center in word and all(c in puzzle for c in word)]

    def display_words(words):
        sbg.clear_word_list()
        score = 0
        pangram_found = False
        for word in words:
            color = "Black"
            if len(word) == 7:
                color = "Blue"
                pangram_found = True
                score += 7
            else:
                score += len(word)
            sbg.add_word(word, color)
        sbg.show_message(f"Total words found: {len(words)}. Total Score: {score}.", "Black")
        if pangram_found:
            sbg.show_message("Pangram found!", "Blue")

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

if __name__ == "__main__":
    spelling_bee()