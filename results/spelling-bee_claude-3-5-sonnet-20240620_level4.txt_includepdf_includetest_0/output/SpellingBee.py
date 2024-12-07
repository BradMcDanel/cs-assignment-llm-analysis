from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

def load_dictionary():
    with open(DICTIONARY_FILE, 'r') as file:
        return set(word.strip().lower() for word in file)

def is_valid_puzzle(letters):
    return (len(letters) == 7 and
            letters.isalpha() and
            len(set(letters)) == 7)

def word_is_valid(word, center, letters):
    return (len(word) >= 4 and
            center in word and
            all(letter in letters for letter in word))

def calculate_score(word, letters):
    score = len(word)
    if len(word) == 4:
        score = 1
    if set(word) == set(letters):
        score += 7
    return score

def spelling_bee():
    sbg = SpellingBeeGraphics()
    dictionary = load_dictionary()
    found_words = set()
    total_score = 0

    def puzzle_action(s):
        letters = s.upper()
        if is_valid_puzzle(letters):
            sbg.set_beehive_letters(letters)
            sbg.show_message("Puzzle set successfully!")
        else:
            sbg.show_message("Invalid puzzle. Please enter 7 unique letters.", "Red")

    def solve_action(s):
        letters = sbg.get_beehive_letters().lower()
        if not letters:
            sbg.show_message("Please set a valid puzzle first.", "Red")
            return

        center = letters[0]
        sbg.clear_word_list()
        found_words.clear()
        nonlocal total_score
        total_score = 0
        word_count = 0

        for word in dictionary:
            if word_is_valid(word, center, letters):
                score = calculate_score(word, letters)
                color = "Blue" if set(word) == set(letters) else "Black"
                sbg.add_word(f"{word} ({score})", color)
                found_words.add(word)
                total_score += score
                word_count += 1

        sbg.show_message(f"Found {word_count} words. Total score: {total_score}")

    def word_action(s):
        letters = sbg.get_beehive_letters().lower()
        if not letters:
            sbg.show_message("Please set a valid puzzle first.", "Red")
            return

        word = s.lower()
        center = letters[0]

        if word in found_words:
            sbg.show_message("Word already found!", "Red")
        elif word not in dictionary:
            sbg.show_message("Word not in dictionary.", "Red")
        elif not word_is_valid(word, center, letters):
            if len(word) < 4:
                sbg.show_message("Word too short.", "Red")
            elif center not in word:
                sbg.show_message("Word doesn't contain center letter.", "Red")
            else:
                sbg.show_message("Word contains invalid letters.", "Red")
        else:
            score = calculate_score(word, letters)
            color = "Blue" if set(word) == set(letters) else "Black"
            sbg.add_word(f"{word} ({score})", color)
            found_words.add(word)
            nonlocal total_score
            total_score += score
            sbg.show_message(f"Word accepted! Score: {score}. Total score: {total_score}")
            sbg.set_field("Word", "")

    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)
    sbg.add_field("Word", word_action)

if __name__ == "__main__":
    spelling_bee()