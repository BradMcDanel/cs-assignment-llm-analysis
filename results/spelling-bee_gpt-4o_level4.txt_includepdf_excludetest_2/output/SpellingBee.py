from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

def spelling_bee():
    def puzzle_action(s):
        if is_legal_puzzle(s):
            sbg.set_beehive_letters(s)
            sbg.show_message("Puzzle set successfully", "Green")
        else:
            sbg.show_message("Invalid puzzle. Ensure it has 7 unique letters.", "Red")

    def solve_action(s):
        sbg.clear_word_list()
        words, total_score = find_words(sbg.get_beehive_letters())
        for word, score in words:
            color = "Blue" if score > len(word) else "Black"
            sbg.add_word(f"{word} ({score})", color)
        sbg.show_message(f"Found {len(words)} words with a total score of {total_score}", "Green")

    def is_legal_puzzle(puzzle):
        return len(puzzle) == 7 and puzzle.isalpha() and len(set(puzzle)) == 7

    def find_words(beehive_letters):
        center_letter = beehive_letters[0].lower()
        allowed_letters = set(beehive_letters.lower())
        words = []
        total_score = 0

        with open(DICTIONARY_FILE, "r") as file:
            for word in file:
                word = word.strip()
                if (len(word) >= 4 and 
                    center_letter in word and 
                    set(word).issubset(allowed_letters)):
                    score = len(word) + (7 if len(set(word)) == 7 else 0)
                    words.append((word, score))
                    total_score += score

        return words, total_score

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

# Startup code
if __name__ == "__main__":
    spelling_bee()