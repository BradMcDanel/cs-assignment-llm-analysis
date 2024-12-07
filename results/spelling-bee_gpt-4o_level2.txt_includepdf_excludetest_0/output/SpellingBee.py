from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

def spelling_bee():
    
    def is_legal_puzzle(puzzle):
        if len(puzzle) != 7:
            return False, "The puzzle must contain exactly seven characters."
        if not puzzle.isalpha():
            return False, "Every character must be one of the 26 letters."
        if len(set(puzzle)) != 7:
            return False, "No letter may appear more than once in the puzzle."
        return True, ""
    
    def puzzle_action(s):
        puzzle = s.strip().upper()
        is_legal, message = is_legal_puzzle(puzzle)
        if is_legal:
            sbg.set_beehive_letters(puzzle)
            sbg.show_message("Puzzle set!", "Green")
        else:
            sbg.show_message(message, "Red")

    def solve_action(s):
        sbg.clear_word_list()
        puzzle = sbg.get_beehive_letters().lower()
        center_letter = puzzle[0]

        with open(DICTIONARY_FILE) as file:
            dictionary = file.read().splitlines()

        found_words = []
        total_score = 0
        for word in dictionary:
            if len(word) >= 4 and all(c in puzzle for c in word) and center_letter in word:
                score = len(word)
                if set(word) == set(puzzle):
                    score += 7  # Pangram bonus
                    sbg.add_word(f"{word} ({score})", "Blue")
                else:
                    sbg.add_word(f"{word} ({score})")
                found_words.append(word)
                total_score += score

        sbg.show_message(f"Found {len(found_words)} words. Total score: {total_score}")

    def word_action(s):
        word = s.strip().lower()
        puzzle = sbg.get_beehive_letters().lower()
        center_letter = puzzle[0]
        
        with open(DICTIONARY_FILE) as file:
            dictionary = set(file.read().splitlines())

        if word in dictionary:
            if len(word) >= 4 and all(c in puzzle for c in word) and center_letter in word:
                if word not in found_words:
                    score = len(word)
                    if set(word) == set(puzzle):
                        score += 7  # Pangram bonus
                        sbg.add_word(f"{word} ({score})", "Blue")
                    else:
                        sbg.add_word(f"{word} ({score})")
                    found_words.add(word)
                    total_score += score
                    sbg.set_field("Word", "")
                    sbg.show_message(f"Word added! Total score: {total_score}")
                else:
                    sbg.show_message("Word already found.", "Red")
            else:
                sbg.show_message("Word does not meet puzzle requirements.", "Red")
        else:
            sbg.show_message("Word not in dictionary.", "Red")

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)
    sbg.add_field("Word", word_action)

# Startup code
if __name__ == "__main__":
    spelling_bee()