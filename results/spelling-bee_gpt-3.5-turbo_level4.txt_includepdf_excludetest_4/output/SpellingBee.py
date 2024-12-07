from SpellingBeeGraphics import SpellingBeeGraphics

DICTIONARY_FILE = "EnglishWords.txt"

def spelling_bee():
    def puzzle_action(s):
        letters = sbg.get_field("Puzzle")
        if validate_puzzle(letters):
            sbg.set_beehive_letters(letters)
        else:
            sbg.show_message("Invalid Puzzle. Must be 7 unique alphabetic characters.", "Red")

    def solve_action(s):
        sbg.clear_word_list()
        letters = sbg.get_beehive_letters()
        dictionary = read_dictionary(DICTIONARY_FILE)
        for word in dictionary:
            if validate_word(word, letters):
                sbg.add_word(word)
    
    def validate_puzzle(letters):
        if len(letters) != 7:
            return False
        if not letters.isalpha() or len(set(letters)) != 7:
            return False
        return True

    def validate_word(word, letters):
        if len(word) < 4 or not all(c in letters for c in word) or letters[0] not in word:
            return False
        return True

    def read_dictionary(filename):
        with open(filename, "r") as file:
            return [line.strip() for line in file]

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

if __name__ == "__main__":
    spelling_bee()