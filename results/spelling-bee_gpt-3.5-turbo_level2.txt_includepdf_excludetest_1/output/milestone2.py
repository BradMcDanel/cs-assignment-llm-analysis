# Your code for Milestone #2 here

import re

def solve_action(s):
    puzzle = sbg.get_beehive_letters()
    dictionary = read_dictionary(DICTIONARY_FILE)
    for word in dictionary:
        if check_word_validity(word, puzzle):
            sbg.add_word(word)
    
def read_dictionary(filename):
    with open(filename, 'r') as file:
        return [word.strip() for word in file]

def check_word_validity(word, puzzle):
    if len(word) < 4:
        return False
    if not set(word).issubset(set(puzzle)):
        return False
    if puzzle[0] not in word:
        return False
    return True