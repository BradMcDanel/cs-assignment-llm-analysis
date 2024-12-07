from SpellingBeeGraphics import SpellingBeeGraphics

DICTIONARY_FILE = "EnglishWords.txt"

def spelling_bee():
    sbg = SpellingBeeGraphics()
    words = load_dictionary(DICTIONARY_FILE)
    found_words = set()
    total_score = 0

    def puzzle_action(s):
        if is_valid_puzzle(s):
            sbg.set_beehive_letters(s)
            sbg.show_message("Puzzle set! You can now enter words or click Solve.")
        else:
            sbg.show_message("Invalid puzzle. Please enter 7 unique letters.", "Red")

    def word_action(s):
        word = s.lower()
        if is_valid_word(word, sbg.get_beehive_letters()):
            if word in found_words:
                sbg.show_message("Word already found!", "Red")
            elif word in words:
                found_words.add(word)
                score = score_word(word, sbg.get_beehive_letters())
                sbg.add_word(f"{word} ({score})", "Blue" if is_pangram(word, sbg.get_beehive_letters()) else "Black")
                nonlocal total_score
                total_score += score
                update_score_message(len(found_words), total_score)
                sbg.set_field("Word", "")
            else:
                sbg.show_message("Word not in dictionary.", "Red")
        else:
            sbg.show_message("Invalid word. Check length, letters, and center letter.", "Red")

    def solve_action(s):
        sbg.clear_word_list()
        found_words.clear()
        nonlocal total_score
        total_score = 0
        center = sbg.get_beehive_letters()[0].lower()
        valid_words = [word for word in words if is_valid_word(word, sbg.get_beehive_letters())]
        for word in valid_words:
            score = score_word(word, sbg.get_beehive_letters())
            sbg.add_word(f"{word} ({score})", "Blue" if is_pangram(word, sbg.get_beehive_letters()) else "Black")
            total_score += score
        update_score_message(len(valid_words), total_score)

    def update_score_message(word_count, score):
        sbg.show_message(f"Words: {word_count}, Score: {score}")

    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_field("Word", word_action)
    sbg.add_button("Solve", solve_action)

def load_dictionary(filename):
    with open(filename, 'r') as file:
        return set(word.strip().lower() for word in file)

def is_valid_puzzle(puzzle):
    return len(puzzle) == 7 and puzzle.isalpha() and len(set(puzzle)) == 7

def is_valid_word(word, puzzle):
    puzzle = puzzle.lower()
    return (len(word) >= 4 and
            set(word).issubset(set(puzzle)) and
            puzzle[0] in word)

def is_pangram(word, puzzle):
    return set(word) == set(puzzle.lower())

def score_word(word, puzzle):
    base_score = len(word) if len(word) > 4 else 1
    return base_score + (7 if is_pangram(word, puzzle) else 0)

if __name__ == "__main__":
    spelling_bee()