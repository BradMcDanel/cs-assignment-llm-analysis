from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

def spelling_bee():

    found_words = set()

    def load_dictionary(file_path):
        with open(file_path, 'r') as file:
            return set(word.strip().lower() for word in file)

    def is_legal_puzzle(letters):
        return len(letters) == 7 and letters.isalpha() and len(set(letters)) == 7

    def is_valid_word(word, letters, center_letter):
        return (
            len(word) >= 4 and 
            set(word).issubset(letters) and 
            center_letter in word
        )

    def calculate_score(word, letters):
        score = len(word) if len(word) > 4 else 1
        if set(word) == set(letters):
            score += 7  # Pangram bonus
        return score

    def puzzle_action(letters):
        if is_legal_puzzle(letters):
            sbg.set_beehive_letters(letters.upper())
            sbg.show_message("Puzzle accepted", "Green")
        else:
            sbg.show_message("Puzzle must have 7 unique alphabetic characters", "Red")

    def solve_action(s):
        sbg.clear_word_list()
        dictionary = load_dictionary(DICTIONARY_FILE)
        letters = sbg.get_beehive_letters().lower()
        center_letter = letters[0]

        total_score = 0
        valid_words = []

        for word in dictionary:
            if is_valid_word(word, letters, center_letter):
                valid_words.append(word)
                word_score = calculate_score(word, letters)
                total_score += word_score
                color = "Blue" if set(word) == set(letters) else "Black"
                sbg.add_word(f"{word} ({word_score})", color)

        sbg.show_message(f"Found {len(valid_words)} words, Total Score: {total_score}", "Green")

    def word_action(word):
        word = word.lower()
        dictionary = load_dictionary(DICTIONARY_FILE)
        letters = sbg.get_beehive_letters().lower()
        center_letter = letters[0]

        if word in found_words:
            sbg.show_message(f"You've already found the word: {word}", "Red")
        elif word not in dictionary:
            sbg.show_message(f"The word {word} is not in the dictionary.", "Red")
        elif not is_valid_word(word, letters, center_letter):
            sbg.show_message(f"The word {word} is invalid.", "Red")
        else:
            found_words.add(word)
            word_score = calculate_score(word, letters)
            color = "Blue" if set(word) == set(letters) else "Black"
            sbg.add_word(f"{word} ({word_score})", color)
            sbg.show_message(f"Word accepted. Total Score: {sum(calculate_score(w, letters) for w in found_words)}", "Green")
            sbg.set_field("Word", "")

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)
    sbg.add_field("Word", word_action, 20)

# Startup code
if __name__ == "__main__":
    spelling_bee()