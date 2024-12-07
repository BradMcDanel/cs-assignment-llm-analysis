from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

def spelling_bee():
    found_words = set()
    
    def puzzle_action(s):
        if is_valid_puzzle(s):
            sbg.set_beehive_letters(s)
            sbg.show_message("")
            found_words.clear()
        else:
            sbg.show_message("Invalid puzzle. Must have 7 unique letters.", "Red")

    def is_valid_puzzle(puzzle):
        return len(puzzle) == 7 and len(set(puzzle)) == 7 and puzzle.isalpha()

    def solve_action(s):
        sbg.clear_word_list()
        beehive_letters = sbg.get_beehive_letters().lower()
        center_letter = beehive_letters[0]
        legal_words = find_legal_words(beehive_letters, center_letter)
        total_score = 0
        for word in legal_words:
            score = calculate_score(word, beehive_letters)
            total_score += score
            color = "Blue" if is_pangram(word, beehive_letters) else "Black"
            sbg.add_word(f"{word} ({score})", color)
        sbg.show_message(f"Total words: {len(legal_words)}, Total score: {total_score}")

    def find_legal_words(beehive_letters, center_letter):
        with open(DICTIONARY_FILE) as f:
            words = f.read().splitlines()
        legal_words = []
        for word in words:
            if (len(word) >= 4 and center_letter in word and
                all(char in beehive_letters for char in word)):
                legal_words.append(word)
        return legal_words

    def calculate_score(word, beehive_letters):
        if is_pangram(word, beehive_letters):
            return len(word) + 7
        return len(word)

    def is_pangram(word, beehive_letters):
        return all(char in word for char in beehive_letters)

    def word_action(s):
        word = s.lower()
        beehive_letters = sbg.get_beehive_letters().lower()
        center_letter = beehive_letters[0]
        if word in found_words:
            sbg.show_message("Word already found.", "Red")
        elif not is_valid_word(word, beehive_letters, center_letter):
            sbg.show_message("Invalid word.", "Red")
        else:
            score = calculate_score(word, beehive_letters)
            color = "Blue" if is_pangram(word, beehive_letters) else "Black"
            sbg.add_word(f"{word} ({score})", color)
            found_words.add(word)
            sbg.show_message("")
            update_score_and_word_count(found_words)

    def is_valid_word(word, beehive_letters, center_letter):
        with open(DICTIONARY_FILE) as f:
            words = set(f.read().splitlines())
        return (word in words and len(word) >= 4 and center_letter in word and
                all(char in beehive_letters for char in word))

    def update_score_and_word_count(found_words):
        total_score = sum(calculate_score(word, sbg.get_beehive_letters().lower()) for word in found_words)
        sbg.show_message(f"Total words: {len(found_words)}, Total score: {total_score}")

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_field("Word", word_action)
    sbg.add_button("Solve", solve_action)

if __name__ == "__main__":
    spelling_bee()