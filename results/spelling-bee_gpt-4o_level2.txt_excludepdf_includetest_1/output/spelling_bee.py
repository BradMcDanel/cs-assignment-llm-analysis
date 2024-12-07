from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

# Helper functions
def is_legal_puzzle(letters):
    if len(letters) != 7:
        return False, "The puzzle must contain exactly seven characters."
    if not all(char.isalpha() for char in letters):
        return False, "Every character must be a letter."
    if len(set(letters)) != 7:
        return False, "No letter may appear more than once."
    return True, ""

def read_dictionary():
    with open(DICTIONARY_FILE) as file:
        return set(word.strip().lower() for word in file)

def is_legal_word(word, letters, center_letter):
    if len(word) < 4:
        return False
    if center_letter not in word:
        return False
    if any(letter not in letters for letter in word):
        return False
    return True

def calculate_score(word, beehive_letters):
    score = len(word)
    if set(word) == set(beehive_letters):
        score += 7  # Pangram bonus
    return score

def spelling_bee():
    dictionary = read_dictionary()
    found_words = set()
    
    def puzzle_action(letters):
        letters = letters.upper()
        valid, message = is_legal_puzzle(letters)
        if valid:
            sbg.set_beehive_letters(letters)
            sbg.show_message("Puzzle set successfully!", "Green")
        else:
            sbg.show_message(message, "Red")

    def solve_action(s):
        sbg.clear_word_list()
        beehive_letters = sbg.get_beehive_letters().lower()
        center_letter = beehive_letters[0]
        total_score = 0
        word_count = 0
        for word in dictionary:
            if is_legal_word(word, beehive_letters, center_letter):
                if word not in found_words:
                    score = calculate_score(word, beehive_letters)
                    total_score += score
                    word_count += 1
                    color = "Blue" if score > len(word) else "Black"
                    sbg.add_word(f"{word} ({score})", color)
        sbg.show_message(f"Total words found: {word_count}, Total score: {total_score}", "Green")

    def word_action(word):
        word = word.lower()
        beehive_letters = sbg.get_beehive_letters().lower()
        center_letter = beehive_letters[0]
        if word in found_words:
            sbg.show_message("Word already found.", "Red")
        elif word not in dictionary:
            sbg.show_message("Word not in dictionary.", "Red")
        elif not is_legal_word(word, beehive_letters, center_letter):
            sbg.show_message("Word does not meet puzzle criteria.", "Red")
        else:
            found_words.add(word)
            score = calculate_score(word, beehive_letters)
            color = "Blue" if score > len(word) else "Black"
            sbg.add_word(f"{word} ({score})", color)
            sbg.show_message("Word added successfully!", "Green")
            sbg.set_field("Word", "")

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)
    sbg.add_field("Word", word_action)

# Startup code
if __name__ == "__main__":
    spelling_bee()