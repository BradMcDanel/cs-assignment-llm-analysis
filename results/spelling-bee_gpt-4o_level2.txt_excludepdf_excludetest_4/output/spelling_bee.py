from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

def spelling_bee():
    # Initialize the graphics object
    sbg = SpellingBeeGraphics()
    
    # Add the Puzzle field and Solve button
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

    # Load dictionary words
    dictionary = load_dictionary(DICTIONARY_FILE)

    def puzzle_action(s):
        if is_legal_puzzle(s):
            sbg.set_beehive_letters(s)
            sbg.show_message("")
        else:
            sbg.show_message("Puzzle must have 7 unique letters.", "Red")

    def solve_action(s):
        beehive_letters = sbg.get_beehive_letters()
        center_letter = beehive_letters[0]
        valid_words = find_valid_words(beehive_letters, center_letter, dictionary)
        
        sbg.clear_word_list()
        total_score = 0
        pangram_count = 0
        
        for word in valid_words:
            score = calculate_word_score(word, beehive_letters)
            total_score += score
            if set(word) == set(beehive_letters):
                sbg.add_word(word, "Blue")
                pangram_count += 1
            else:
                sbg.add_word(word)

        sbg.show_message(f"Found {len(valid_words)} words with a total score of {total_score}. {pangram_count} pangram(s).")

    def load_dictionary(filename):
        with open(filename, 'r') as file:
            return [line.strip() for line in file]

    def is_legal_puzzle(puzzle):
        if len(puzzle) != 7:
            return False
        if not all(char.isalpha() for char in puzzle):
            return False
        if len(set(puzzle)) != 7:
            return False
        return True

    def find_valid_words(beehive_letters, center_letter, dictionary):
        valid_words = []
        for word in dictionary:
            if len(word) < 4:
                continue
            if center_letter not in word:
                continue
            if not all(char in beehive_letters for char in word):
                continue
            valid_words.append(word)
        return valid_words

    def calculate_word_score(word, beehive_letters):
        score = len(word) if len(word) > 4 else 1
        if set(word) == set(beehive_letters):
            score += 7  # Pangram bonus
        return score

if __name__ == "__main__":
    spelling_bee()