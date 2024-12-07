from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

def spelling_bee():
    
    def is_legal_puzzle(puzzle):
        # Check if the puzzle has exactly 7 unique letters and all are alphabets
        return len(puzzle) == 7 and puzzle.isalpha() and len(set(puzzle)) == 7

    def read_dictionary():
        # Read dictionary words into a set for quick lookup
        with open(DICTIONARY_FILE, 'r') as file:
            return set(word.strip().lower() for word in file.readlines())

    def is_valid_word(word, beehive_letters, center_letter):
        # Check if the word is at least 4 letters, contains the center letter, and only uses beehive letters
        return (len(word) >= 4 and 
                center_letter in word and
                all(char in beehive_letters for char in word))

    def calculate_score(word, beehive_letters):
        # Calculate word score
        score = len(word) if len(word) > 4 else 1
        if set(word) == set(beehive_letters):
            score += 7  # Pangram bonus
        return score

    def puzzle_action(s):
        s = s.lower().strip()
        if is_legal_puzzle(s):
            sbg.set_beehive_letters(s.upper())
            sbg.show_message("Puzzle set successfully!", "Green")
        else:
            sbg.show_message("Invalid puzzle! Ensure it's 7 unique letters.", "Red")

    def solve_action(s):
        sbg.clear_word_list()
        beehive_letters = sbg.get_beehive_letters().lower()
        if not beehive_letters:
            sbg.show_message("Set the puzzle first!", "Red")
            return

        center_letter = beehive_letters[0]
        dictionary = read_dictionary()
        found_words = []
        total_score = 0

        for word in dictionary:
            if is_valid_word(word, beehive_letters, center_letter):
                score = calculate_score(word, beehive_letters)
                total_score += score
                color = "Blue" if score > len(word) else "Black"
                sbg.add_word(f"{word} ({score})", color)
                found_words.append(word)
        
        sbg.show_message(f"Found {len(found_words)} words. Total score: {total_score}", "Green")

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

# Startup code
if __name__ == "__main__":
    spelling_bee()