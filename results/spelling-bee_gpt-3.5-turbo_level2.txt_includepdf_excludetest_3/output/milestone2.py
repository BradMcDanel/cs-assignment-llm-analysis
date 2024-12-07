from SpellingBeeGraphics import SpellingBeeGraphics

def solve_action(s):
    dictionary = read_dictionary(DICTIONARY_FILE)
    beehive = sbg.get_beehive_letters()
    for word in dictionary:
        if is_valid_word(word, beehive):
            sbg.add_word(word)

def read_dictionary(file):
    with open(file, 'r') as f:
        return [line.strip() for line in f]

def is_valid_word(word, beehive):
    return len(word) >= 4 and all(letter in beehive for letter in word) and beehive[0] in word

if __name__ == "__main__":
    solve_action()