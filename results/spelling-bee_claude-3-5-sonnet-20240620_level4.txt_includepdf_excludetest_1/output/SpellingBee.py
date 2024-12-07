from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

def spelling_bee():
    # Initialize the graphics
    sbg = SpellingBeeGraphics()

    # Read the dictionary
    with open(DICTIONARY_FILE, 'r') as f:
        dictionary = set(word.strip().lower() for word in f)

    # Keep track of found words and score
    found_words = set()
    total_score = 0

    def is_valid_puzzle(letters):
        return (len(letters) == 7 and
                letters.isalpha() and
                len(set(letters)) == 7)

    def puzzle_action(s):
        if is_valid_puzzle(s):
            sbg.set_beehive_letters(s.upper())
            sbg.show_message("Puzzle set successfully!")
        else:
            sbg.show_message("Invalid puzzle. Please enter 7 unique letters.", "Red")

    def is_valid_word(word, puzzle):
        center = puzzle[0].lower()
        puzzle_set = set(puzzle.lower())
        return (len(word) >= 4 and
                set(word).issubset(puzzle_set) and
                center in word)

    def calculate_score(word):
        if len(word) == 4:
            return 1
        elif len(set(word)) == 7:
            return len(word) + 7
        else:
            return len(word)

    def solve_action(s):
        puzzle = sbg.get_beehive_letters()
        sbg.clear_word_list()
        found_words.clear()
        nonlocal total_score
        total_score = 0

        for word in dictionary:
            if is_valid_word(word, puzzle):
                score = calculate_score(word)
                total_score += score
                found_words.add(word)
                color = "Blue" if len(set(word)) == 7 else "Black"
                sbg.add_word(f"{word} ({score})", color)

        sbg.show_message(f"Found {len(found_words)} words. Total score: {total_score}")

    def word_action(s):
        puzzle = sbg.get_beehive_letters()
        word = s.lower()

        if word in found_words:
            sbg.show_message("Word already found!", "Red")
        elif word not in dictionary:
            sbg.show_message("Word not in dictionary.", "Red")
        elif not is_valid_word(word, puzzle):
            if len(word) < 4:
                sbg.show_message("Word too short.", "Red")
            elif puzzle[0].lower() not in word:
                sbg.show_message("Word doesn't contain center letter.", "Red")
            else:
                sbg.show_message("Word contains invalid letters.", "Red")
        else:
            score = calculate_score(word)
            found_words.add(word)
            nonlocal total_score
            total_score += score
            color = "Blue" if len(set(word)) == 7 else "Black"
            sbg.add_word(f"{word} ({score})", color)
            sbg.set_field("Word", "")
            sbg.show_message(f"Word added! Score: {score}. Total: {total_score}")

    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)
    sbg.add_field("Word", word_action)

if __name__ == "__main__":
    spelling_bee()