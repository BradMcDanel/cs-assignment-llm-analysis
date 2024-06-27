from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

def spelling_bee():
    # Read the dictionary
    with open(DICTIONARY_FILE, 'r') as f:
        dictionary = set(word.strip().lower() for word in f)

    sbg = SpellingBeeGraphics()
    found_words = set()
    total_score = 0
    word_count = 0

    def is_valid_puzzle(letters):
        return (len(letters) == 7 and
                letters.isalpha() and
                len(set(letters)) == 7)

    def calculate_word_score(word):
        score = len(word)
        if score == 4:
            return 1
        if len(set(word)) == 7:
            return score + 7
        return score

    def update_score_display():
        sbg.show_message(f"Words: {word_count}, Score: {total_score}")

    def is_valid_word(word, center_letter, puzzle_letters):
        return (len(word) >= 4 and
                center_letter in word and
                set(word).issubset(puzzle_letters) and
                word in dictionary and
                word not in found_words)

    def add_valid_word(word, is_computer_solve=False):
        nonlocal total_score, word_count
        score = calculate_word_score(word)
        total_score += score
        word_count += 1
        color = "Blue" if len(set(word)) == 7 else "Black"
        sbg.add_word(f"{word} ({score})", color)
        found_words.add(word)
        if not is_computer_solve:
            update_score_display()

    def puzzle_action(s):
        if is_valid_puzzle(s):
            sbg.set_beehive_letters(s.upper())
            sbg.show_message("Puzzle set successfully!")
            sbg.clear_word_list()
            found_words.clear()
            nonlocal total_score, word_count
            total_score = 0
            word_count = 0
        else:
            sbg.show_message("Invalid puzzle! Please enter 7 unique letters.", "Red")

    def solve_action(s):
        puzzle_letters = set(sbg.get_beehive_letters().lower())
        center_letter = sbg.get_beehive_letters()[0].lower()
        sbg.clear_word_list()
        found_words.clear()
        nonlocal total_score, word_count
        total_score = 0
        word_count = 0

        for word in dictionary:
            if is_valid_word(word, center_letter, puzzle_letters):
                add_valid_word(word, True)

        update_score_display()

    def word_action(s):
        puzzle_letters = set(sbg.get_beehive_letters().lower())
        center_letter = sbg.get_beehive_letters()[0].lower()
        word = s.lower()

        if is_valid_word(word, center_letter, puzzle_letters):
            add_valid_word(word)
            sbg.set_field("Word", "")
        else:
            if word in found_words:
                sbg.show_message("Word already found!", "Red")
            elif len(word) < 4:
                sbg.show_message("Word too short!", "Red")
            elif center_letter not in word:
                sbg.show_message("Word doesn't contain center letter!", "Red")
            elif not set(word).issubset(puzzle_letters):
                sbg.show_message("Word contains invalid letters!", "Red")
            else:
                sbg.show_message("Word not in dictionary!", "Red")

    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)
    sbg.add_field("Word", word_action)

# Startup code
if __name__ == "__main__":
    spelling_bee()