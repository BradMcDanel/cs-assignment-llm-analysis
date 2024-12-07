# Helper functions for Wordle game

def get_occurrences(word):
    occurrences = {}
    for letter in word:
        if letter in occurrences:
            occurrences[letter] += 1
        else:
            occurrences[letter] = 1
    return occurrences

def check_matching_letters(word, guess):
    matching = {}
    for i in range(len(word)):
        if word[i] == guess[i]:
            matching[word[i]] = 'green'
        elif guess[i] in word:
            matching[guess[i]] = 'yellow'
        else:
            matching[guess[i]] = 'gray'
    return matching