from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

def spelling_bee():
    def read_dictionary():
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
        if score == 4:
            score = 1
        if set(word) == set(letters):
            score += 7  # Pangram bonus
        return score

    def puzzle_action(s):
        letters = s.upper()
        if is_valid_puzzle(letters):
            sbg.set_beehive_letters(letters)
            sbg.show_message("")
        else:
            sbg.show_message("Invalid puzzle. Please enter 7 unique letters.", "Red")

    def solve_action(s):
        letters = sbg.get_beehive_letters().lower()
        center = letters[0]
        words = read_dictionary()
        valid_words = []
        total_score = 0
        word_count = 0

        sbg.clear_word_list()
        for word in words:
            if is_valid_word(word, center, letters):
                score = calculate_score(word, letters)
                color = "Blue" if set(word) == set(letters) else "Black"
                sbg.add_word(f"{word} ({score})", color)
                valid_words.append(word)
                total_score += score
                word_count += 1

        sbg.show_message(f"Found {word_count} words. Total score: {total_score}")

    def word_action(s):
        letters = sbg.get_beehive_letters().lower()
        center = letters[0]
        word = s.lower()
        words = read_dictionary()

        if word not in words:
            sbg.show_message("Word not in dictionary.", "Red")
        elif not is_valid_word(word, center, letters):
            if len(word) < 4:
                sbg.show_message("Word must be at least 4 letters long.", "Red")
            elif center not in word:
                sbg.show_message("Word must contain the center letter.", "Red")
            else:
                sbg.show_message("Word contains invalid letters.", "Red")
        else:
            score = calculate_score(word, letters)
            color = "Blue" if set(word) == set(letters) else "Black"
            sbg.add_word(f"{word} ({score})", color)
            current_score = int(sbg.get_field("Score") or "0")
            current_words = int(sbg.get_field("Words") or "0")
            sbg.set_field("Score", str(current_score + score))
            sbg.set_field("Words", str(current_words + 1))
            sbg.show_message(f"Good! Current score: {current_score + score}")
        
        sbg.set_field("Word", "")  # Clear the word field

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action, 7)
    sbg.add_field("Word", word_action, 15)
    sbg.add_button("Solve", solve_action)
    sbg.add_field("Words", None, 5)
    sbg.add_field("Score", None, 5)

# Startup code
if __name__ == "__main__":
    spelling_bee()