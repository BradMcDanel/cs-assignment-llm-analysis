from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

def spelling_bee():
    def puzzle_action(s):
        # Validate the input string for the puzzle
        if not is_valid_puzzle(s):
            sbg.show_message("Invalid puzzle: must contain exactly 7 unique letters", "Red")
            return
        sbg.set_beehive_letters(s.upper())
    
    def solve_action(s):
        sbg.clear_word_list()
        words, total_score, total_words = find_words(sbg.get_beehive_letters())
        for word, score in words.items():
            color = "Blue" if len(set(word)) == 7 else "Black"
            sbg.add_word(f"{word} ({score})", color)
        sbg.show_message(f"Total words: {total_words}, Total score: {total_score}")
    
    def is_valid_puzzle(puzzle):
        return len(puzzle) == 7 and puzzle.isalpha() and len(set(puzzle)) == 7
    
    def read_dictionary():
        with open(DICTIONARY_FILE, 'r') as file:
            return {line.strip().lower() for line in file}
    
    def find_words(letters):
        dictionary = read_dictionary()
        center_letter = letters[0].lower()
        legal_words = {}
        total_score = 0

        for word in dictionary:
            if len(word) >= 4 and center_letter in word and all(c in letters.lower() for c in word):
                score = len(word) + (7 if len(set(word)) == 7 else 0)
                legal_words[word] = score
                total_score += score

        return legal_words, total_score, len(legal_words)

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

# Startup code
if __name__ == "__main__":
    spelling_bee()