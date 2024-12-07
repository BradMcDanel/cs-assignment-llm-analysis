from SpellingBeeGraphics import SpellingBeeGraphics

def spelling_bee():
    def puzzle_action(s):
        puzzle = sbg.get_field("Puzzle")
        if is_legal_puzzle(puzzle):
            sbg.set_beehive_letters(puzzle.upper())
        else:
            sbg.show_message("Invalid puzzle. Please enter exactly 7 unique letters.", "Red")

    def find_word_action(s):
        word = sbg.get_field("Word").lower()
        beehive = sbg.get_beehive_letters()
        if is_valid_word(word, beehive):
            sbg.add_word(word)
            sbg.show_message("Word found. Total words: " + str(len(sbg._wordlist)))
            sbg.set_field("Word", "")
        else:
            error = "Invalid word. "
            if not word.isalpha():
                error += "Word must contain only alphabetic characters. "
            if len(set(word)) != len(word):
                error += "Word must not contain repeated characters. "
            if len(word) < 4:
                error += "Word must be at least 4 letters long. "
            if beehive[0] not in word:
                error += "Word must contain the center letter."
            sbg.show_message(error, "Red")

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_field("Word", find_word_action)
    sbg.add_button("Solve", solve_action)

if __name__ == "__main__":
    spelling_bee()