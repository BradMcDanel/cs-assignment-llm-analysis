from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

# Starter program
def spelling_bee():
    found_words = set()
    total_score = 0

    def puzzle_action(s):
        if is_legal_puzzle(s):
            sbg.set_beehive_letters(s)
            sbg.show_message("Puzzle set successfully", "Green")
        else:
            sbg.show_message("Invalid puzzle. Please enter 7 unique letters.", "Red")

    def is_legal_puzzle(puzzle):
        if len(puzzle) != 7:
            return False
        if not puzzle.isalpha():
            return False
        if len(set(puzzle)) != 7:
            return False
        return True

    def solve_action(s):
        letters = sbg.get_beehive_letters()
        words, total_score = find_legal_words_with_scores(letters)
        sbg.clear_word_list()
        for word, score in words:
            color = "Blue" if is_pangram(word, letters) else "Black"
            sbg.add_word(f"{word} ({score})", color)
        sbg.show_message(f"Total words: {len(words)}, Total score: {total_score}", "Green")

    def word_action(s):
        nonlocal total_score
        word = s.lower()
        letters = sbg.get_beehive_letters()
        if word in found_words:
            sbg.show_message("Word already found.", "Red")
        elif not is_legal_word(word, letters):
            sbg.show_message("Invalid word.", "Red")
        elif word not in dictionary:
            sbg.show_message("Word not in dictionary.", "Red")
        else:
            found_words.add(word)
            score = len(word)
            if is_pangram(word, letters):
                score += 7
            total_score += score
            color = "Blue" if is_pangram(word, letters) else "Black"
            sbg.add_word(f"{word} ({score})", color)
            sbg.show_message(f"Total words: {len(found_words)}, Total score: {total_score}", "Green")
            sbg.set_field("Word", "")

    def find_legal_words_with_scores(letters):
        central_letter = letters[0]
        valid_words = []
        total_score = 0
        with open(DICTIONARY_FILE, 'r') as f:
            dictionary = f.read().splitlines()
            for word in dictionary:
                if (len(word) >= 4 and central_letter in word and
                        all(char in letters for char in word)):
                    score = len(word)
                    if is_pangram(word, letters):
                        score += 7
                    total_score += score
                    valid_words.append((word, score))
        return valid_words, total_score

    def is_legal_word(word, letters):
        if len(word) < 4:
            return False
        if letters[0] not in word:
            return False
        if not all(char in letters for char in word):
            return False
        return True

    def is_pangram(word, letters):
        return all(char in word for char in letters)

    with open(DICTIONARY_FILE, 'r') as f:
        dictionary = set(f.read().splitlines())

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)
    sbg.add_field("Word", word_action)

# Startup code
if __name__ == "__main__":
    spelling_bee()