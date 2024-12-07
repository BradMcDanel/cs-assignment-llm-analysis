from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

# Read dictionary file into a list
def read_dictionary():
    with open(DICTIONARY_FILE, 'r') as file:
        dictionary = [word.strip().lower() for word in file]
    return dictionary

# Check if a word meets the requirements
def is_valid_word(word, puzzle):
    if len(word) < 4:
        return False
    if len(set(word) - set(puzzle)) > 0:
        return False
    if puzzle[0] not in word:
        return False
    return True

def word_action(s):
    word = s.get_field("Word").lower()
    puzzle = s.get_beehive_letters().lower()
    dictionary = read_dictionary()

    if word not in dictionary:
        s.show_message("Word not found in dictionary.", "Red")
    elif len(word) < 4:
        s.show_message("Word must be at least 4 letters long.", "Red")
    elif puzzle[0] not in word:
        s.show_message("Word must contain the center letter.", "Red")
    elif len(set(word) - set(puzzle)) > 0:
        s.show_message("Word contains letters not in the puzzle.", "Red")
    else:
        if is_valid_word(word, puzzle):
            s.add_word(word, "Black")
            s.show_message("Word found! Score: " + str(len(word)), "Black")
            s.clear_word_list()
        else:
            s.show_message("Word did not meet all requirements.", "Red")
            s.clear_field("Word")

def spelling_bee_word_checker():
    sbg = SpellingBeeGraphics()
    sbg.add_field("Word", word_action)

if __name__ == "__main__":
    spelling_bee_word_checker()