from SpellingBeeGraphics import SpellingBeeGraphics

DICTIONARY_FILE = "EnglishWords.txt"

def spelling_bee():
    def is_legal_puzzle(puzzle):
        if len(puzzle) != 7:
            return "Puzzle must contain exactly seven characters."
        if not puzzle.isalpha():
            return "Puzzle must only contain letters."
        if len(set(puzzle)) != 7:
            return "Puzzle must not contain duplicate letters."
        return None
    
    def read_dictionary():
        with open(DICTIONARY_FILE, 'r') as file:
            return {line.strip().lower() for line in file}

    def is_valid_word(word, center_letter, letters_set):
        return (
            len(word) >= 4 and
            center_letter in word and
            all(letter in letters_set for letter in word)
        )

    def calculate_score(word, is_pangram):
        score = len(word) if len(word) > 4 else 1
        return score + 7 if is_pangram else score

    def puzzle_action(s):
        nonlocal beehive, center_letter, letters_set
        error_message = is_legal_puzzle(s)
        if error_message:
            sbg.show_message(error_message, "Red")
        else:
            beehive = s.lower()
            center_letter = beehive[0]
            letters_set = set(beehive)
            sbg.set_beehive_letters(s.upper())
            sbg.show_message("")

    def solve_action(s):
        dictionary = read_dictionary()
        total_words = 0
        total_score = 0
        sbg.clear_word_list()
        for word in dictionary:
            if is_valid_word(word, center_letter, letters_set):
                is_pangram = all(letter in word for letter in letters_set)
                score = calculate_score(word, is_pangram)
                color = "Blue" if is_pangram else "Black"
                sbg.add_word(f"{word} ({score})", color)
                total_words += 1
                total_score += score
        sbg.show_message(f"{total_words} words, {total_score} points.", "Green")

    def word_action(word):
        word = word.lower()
        if word in found_words:
            sbg.show_message("Word already found.", "Red")
            return
        if not is_valid_word(word, center_letter, letters_set):
            sbg.show_message("Invalid word.", "Red")
            return
        if word not in dictionary:
            sbg.show_message("Word not in dictionary.", "Red")
            return

        is_pangram = all(letter in word for letter in letters_set)
        score = calculate_score(word, is_pangram)
        color = "Blue" if is_pangram else "Black"
        sbg.add_word(f"{word} ({score})", color)
        found_words.add(word)
        update_score()

    def update_score():
        total_words = len(found_words)
        total_score = sum(calculate_score(word, all(letter in word for letter in letters_set)) for word in found_words)
        sbg.show_message(f"{total_words} words, {total_score} points.", "Green")

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)
    sbg.add_field("Word", word_action)
    
    dictionary = read_dictionary()
    found_words = set()
    beehive = ""
    center_letter = ""
    letters_set = set()

if __name__ == "__main__":
    spelling_bee()