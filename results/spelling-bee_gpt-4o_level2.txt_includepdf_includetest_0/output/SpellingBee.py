from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

def spelling_bee():
    found_words = set()

    def puzzle_action(s):
        if is_valid_puzzle(s):
            sbg.set_beehive_letters(s.upper())
            sbg.show_message("Puzzle updated!", "Green")
        else:
            sbg.show_message("Invalid puzzle input. Ensure 7 unique letters.", "Red")

    def solve_action(s):
        process_solution(False)

    def word_action(word):
        process_solution(True, word.lower())

    def process_solution(is_user_input, user_word=None):
        sbg.clear_word_list()
        letters = sbg.get_beehive_letters().lower()
        center_letter = letters[0]
        words_found = 0
        total_score = 0
        
        with open(DICTIONARY_FILE, 'r') as file:
            dictionary = file.read().splitlines()

        for word in dictionary:
            if is_valid_word(word, letters, center_letter):
                add_word_to_list(word, letters)
                words_found += 1
                total_score += calculate_score(word, letters)

        if is_user_input:
            if user_word and user_word not in found_words:
                if user_word in dictionary and is_valid_word(user_word, letters, center_letter):
                    add_word_to_list(user_word, letters)
                    found_words.add(user_word)
                else:
                    sbg.show_message("Invalid word entry.", "Red")
            else:
                sbg.show_message("Word already found or invalid.", "Red")
        
        sbg.show_message(f"Found {words_found} words with total score: {total_score}", "Black")

    def add_word_to_list(word, letters):
        score = calculate_score(word, letters)
        color = "Blue" if is_pangram(word, letters) else "Black"
        sbg.add_word(f"{word} ({score})", color)

    def is_valid_puzzle(puzzle):
        return len(puzzle) == 7 and puzzle.isalpha() and len(set(puzzle)) == 7

    def is_valid_word(word, letters, center_letter):
        return (
            len(word) >= 4 and
            all(c in letters for c in word) and
            center_letter in word
        )

    def is_pangram(word, letters):
        return set(word) == set(letters)

    def calculate_score(word, letters):
        score = len(word) if len(word) > 4 else 1
        if is_pangram(word, letters):
            score += 7
        return score

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)
    sbg.add_field("Word", word_action)

if __name__ == "__main__":
    spelling_bee()