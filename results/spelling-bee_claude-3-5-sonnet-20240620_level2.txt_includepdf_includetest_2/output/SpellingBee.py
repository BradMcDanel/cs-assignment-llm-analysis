from SpellingBeeGraphics import SpellingBeeGraphics

DICTIONARY_FILE = "EnglishWords.txt"

def spelling_bee():
    def load_dictionary():
        with open(DICTIONARY_FILE, 'r') as file:
            return set(word.strip().lower() for word in file)

    def is_valid_puzzle(letters):
        return (len(letters) == 7 and
                letters.isalpha() and
                len(set(letters)) == 7)

    def is_valid_word(word, center, letters):
        return (len(word) >= 4 and
                center in word and
                all(letter in letters for letter in word))

    def calculate_score(word, letters):
        score = len(word)
        if len(word) == 4:
            score = 1
        if set(word) == set(letters):
            score += 7  # Pangram bonus
        return score

    def puzzle_action(s):
        if is_valid_puzzle(s):
            sbg.set_beehive_letters(s.upper())
            sbg.show_message("Puzzle set successfully!")
        else:
            sbg.show_message("Invalid puzzle. Please enter 7 unique letters.", "Red")

    def solve_action(s):
        letters = sbg.get_beehive_letters().lower()
        center = letters[0]
        words = [word for word in dictionary if is_valid_word(word, center, letters)]
        
        sbg.clear_word_list()
        total_score = 0
        for word in sorted(words):
            score = calculate_score(word, letters)
            total_score += score
            color = "Blue" if set(word) == set(letters) else "Black"
            sbg.add_word(f"{word} ({score})", color)
        
        sbg.show_message(f"Found {len(words)} words. Total score: {total_score}")

    def word_action(s):
        letters = sbg.get_beehive_letters().lower()
        center = letters[0]
        word = s.lower()

        if word not in dictionary:
            sbg.show_message("Word not in dictionary.", "Red")
        elif not is_valid_word(word, center, letters):
            sbg.show_message("Invalid word for this puzzle.", "Red")
        elif word in found_words:
            sbg.show_message("Word already found.", "Red")
        else:
            score = calculate_score(word, letters)
            color = "Blue" if set(word) == set(letters) else "Black"
            sbg.add_word(f"{word} ({score})", color)
            found_words.add(word)
            total_score[0] += score
            sbg.show_message(f"Good! Score: {total_score[0]}, Words: {len(found_words)}")
        
        sbg.set_field("Word", "")

    dictionary = load_dictionary()
    found_words = set()
    total_score = [0]  # Using a list to make it mutable

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_field("Word", word_action)
    sbg.add_button("Solve", solve_action)

if __name__ == "__main__":
    spelling_bee()