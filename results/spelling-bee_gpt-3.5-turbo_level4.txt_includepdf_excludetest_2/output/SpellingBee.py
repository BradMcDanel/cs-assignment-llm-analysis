from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

# Starter program
def spelling_bee():

    def puzzle_action(sbg):
        letters = sbg.get_field("Puzzle")
        if not is_legal_puzzle(letters):
            sbg.show_message("Puzzle is not legal", "Red")
        else:
            sbg.set_beehive_letters(letters)
    
    def solve_action(sbg):
        letters = sbg.get_beehive_letters()
        dictionary = read_dictionary(DICTIONARY_FILE)
        for word in dictionary:
            if is_legal_word(word, letters):
                sbg.add_word(word)
    
    def is_legal_puzzle(letters):
        if len(letters) != 7:
            return False
        if len(set(letters)) != 7:
            return False
        if not letters.isalpha():
            return False
        return True
    
    def read_dictionary(filename):
        with open(filename, 'r') as file:
            return [line.strip() for line in file]

    def is_legal_word(word, letters):
        if len(word) < 4:
            return False
        if not all(letter in letters for letter in word):
            return False
        if letters[0] not in word:
            return False
        return True

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

if __name__ == "__main__":
    spelling_bee()