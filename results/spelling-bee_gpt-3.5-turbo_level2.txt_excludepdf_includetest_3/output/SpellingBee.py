from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

# Global variables to store puzzle and word list
puzzle_letters = ""
word_list = []
total_score = 0

def read_dictionary():
    with open(DICTIONARY_FILE, 'r') as file:
        return [line.strip().lower() for line in file]

def is_legal_word(word):
    global puzzle_letters
    if len(word) < 4:
        return False
    for char in word:
        if char not in puzzle_letters:
            return False
    if puzzle_letters[0] not in word:
        return False
    return True

def solve_puzzle():
    global word_list, total_score
    dictionary = read_dictionary()
    word_list = []
    total_score = 0
    for word in dictionary:
        if is_legal_word(word):
            word_list.append(word)
            word_score = len(word)
            if len(set(word)) == 7:
                word_score += 7
            total_score += word_score

def spelling_bee():
    def puzzle_action(s):
        global puzzle_letters
        if len(s) == 7 and s.isalpha() and len(set(s)) == 7:
            puzzle_letters = s
            sbg.set_beehive_letters(s.upper())
        else:
            sbg.show_message("Invalid puzzle. Please enter exactly 7 unique alphabetic characters.", "Red")

    def solve_action(s):
        solve_puzzle()
        sbg.clear_word_list()
        for word in word_list:
            sbg.add_word(word, "Black")
        sbg.show_message("Total words found: {}. Total score: {}".format(len(word_list), total_score), "Black")

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

# Startup code
if __name__ == "__main__":
    spelling_bee()