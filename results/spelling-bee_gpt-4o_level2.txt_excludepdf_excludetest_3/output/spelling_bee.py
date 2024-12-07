from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

def spelling_bee():
    
    def is_legal_puzzle(puzzle):
        if len(puzzle) != 7:
            return "Puzzle must contain exactly seven characters."
        if not all(char.isalpha() for char in puzzle):
            return "Puzzle must contain only letters."
        if len(set(puzzle)) != 7:
            return "Each letter must be unique."
        return None

    def puzzle_action(s):
        s = s.upper()
        error_message = is_legal_puzzle(s)
        if error_message:
            sbg.show_message(error_message, "Red")
        else:
            sbg.set_beehive_letters(s)
            sbg.show_message("Puzzle set successfully!", "Green")
    
    def load_dictionary():
        with open(DICTIONARY_FILE) as f:
            return [word.strip().lower() for word in f]

    def is_valid_word(word, puzzle, center_letter):
        return (len(word) >= 4 and
                all(c in puzzle for c in word) and
                center_letter in word)
    
    def calculate_score(word, puzzle):
        base_score = len(word) if len(word) > 4 else 1
        pangram_bonus = 7 if all(l in word for l in puzzle) else 0
        return base_score + pangram_bonus

    def solve_action(s):
        sbg.clear_word_list()
        puzzle = sbg.get_beehive_letters().lower()
        center_letter = puzzle[0]
        dictionary = load_dictionary()
        valid_words = [word for word in dictionary if is_valid_word(word, puzzle, center_letter)]
        total_score = 0
        for word in valid_words:
            score = calculate_score(word, puzzle)
            total_score += score
            color = "Blue" if score > len(word) else "Black"
            sbg.add_word(f"{word} ({score})", color)
        sbg.show_message(f"Found {len(valid_words)} words with a total score of {total_score}.", "Green")

    def user_word_action(word):
        word = word.lower()
        puzzle = sbg.get_beehive_letters().lower()
        center_letter = puzzle[0]
        dictionary = load_dictionary()
        if word in found_words:
            sbg.show_message("Word already found.", "Red")
        elif word not in dictionary:
            sbg.show_message("Word not in dictionary.", "Red")
        elif not is_valid_word(word, puzzle, center_letter):
            sbg.show_message("Word does not meet puzzle criteria.", "Red")
        else:
            score = calculate_score(word, puzzle)
            found_words.add(word)
            total_user_score[0] += score
            color = "Blue" if score > len(word) else "Black"
            sbg.add_word(f"{word} ({score})", color)
            sbg.show_message(f"Total score: {total_user_score[0]}", "Green")
        sbg.set_field("Word", "")

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_field("Word", user_word_action)
    sbg.add_button("Solve", solve_action)

    found_words = set()
    total_user_score = [0]

# Startup code
if __name__ == "__main__":
    spelling_bee()