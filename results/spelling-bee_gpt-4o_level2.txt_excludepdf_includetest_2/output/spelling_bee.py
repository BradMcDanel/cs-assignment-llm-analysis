from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

def spelling_bee():
    found_words = set()

    def is_legal_puzzle(letters):
        return len(letters) == 7 and all(c.isalpha() for c in letters) and len(set(letters)) == 7

    def load_dictionary():
        with open(DICTIONARY_FILE) as f:
            return set(word.strip().lower() for word in f)

    def is_valid_word(word, letters, center_letter):
        return (len(word) >= 4 and center_letter in word and
                all(c in letters for c in word))

    def calculate_score(word, letters):
        score = len(word) if len(word) > 4 else 1
        if all(letter in word for letter in letters):
            score += 7
        return score

    def puzzle_action(s):
        s = s.strip().upper()
        if is_legal_puzzle(s):
            sbg.set_beehive_letters(s)
            sbg.show_message("")
        else:
            sbg.show_message("Invalid puzzle. Ensure 7 unique letters.", "Red")

    def solve_action(s):
        sbg.clear_word_list()
        letters = sbg.get_beehive_letters().lower()
        center_letter = letters[0]

        dictionary = load_dictionary()
        valid_words = [word for word in dictionary if is_valid_word(word, letters, center_letter)]

        total_score = 0
        for word in valid_words:
            score = calculate_score(word, letters)
            color = "Blue" if score > len(word) else "Black"
            sbg.add_word(f"{word} ({score})", color)
            total_score += score

        sbg.show_message(f"Found {len(valid_words)} words. Total score: {total_score}")

    def word_action(word):
        word = word.strip().lower()
        letters = sbg.get_beehive_letters().lower()
        center_letter = letters[0]
        dictionary = load_dictionary()

        if word in found_words:
            sbg.show_message("Word already found.")
        elif word not in dictionary:
            sbg.show_message("Word not in dictionary.")
        elif not is_valid_word(word, letters, center_letter):
            sbg.show_message("Word does not meet puzzle requirements.")
        else:
            found_words.add(word)
            score = calculate_score(word, letters)
            color = "Blue" if score > len(word) else "Black"
            sbg.add_word(f"{word} ({score})", color)
            total_score = sum(calculate_score(w, letters) for w in found_words)
            sbg.show_message(f"Total score: {total_score}")
            sbg.set_field("Word", "")

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)
    sbg.add_field("Word", word_action)

if __name__ == "__main__":
    spelling_bee()