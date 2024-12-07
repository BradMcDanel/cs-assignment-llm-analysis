from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

def spelling_bee():
    found_words = set()

    def puzzle_action(s):
        if is_valid_puzzle(s):
            sbg.set_beehive_letters(s.upper())
            sbg.show_message("")
        else:
            sbg.show_message("Invalid puzzle. Ensure there are 7 unique letters.", "Red")

    def solve_action(s):
        sbg.clear_word_list()
        beehive_letters = sbg.get_beehive_letters().lower()
        center_letter = beehive_letters[0]
        
        dictionary = read_dictionary()
        total_score = 0
        word_count = 0
        for word in dictionary:
            if is_valid_word(word, beehive_letters, center_letter):
                score = calculate_score(word, beehive_letters)
                total_score += score
                word_count += 1
                sbg.add_word(f"{word} ({score})", "Blue" if is_pangram(word, beehive_letters) else "Black")
        
        sbg.show_message(f"{word_count} words, {total_score} points")

    def word_action(word):
        beehive_letters = sbg.get_beehive_letters().lower()
        center_letter = beehive_letters[0]
        
        if word in found_words:
            sbg.show_message("Word already found.", "Red")
        elif not is_valid_word(word, beehive_letters, center_letter):
            sbg.show_message("Invalid word.", "Red")
        elif word not in read_dictionary():
            sbg.show_message("Word not in dictionary.", "Red")
        else:
            score = calculate_score(word, beehive_letters)
            found_words.add(word)
            sbg.add_word(f"{word} ({score})", "Blue" if is_pangram(word, beehive_letters) else "Black")
            sbg.show_message(f"{len(found_words)} words, {sum(calculate_score(w, beehive_letters) for w in found_words)} points")
            sbg.set_field("Word", "")

    def is_valid_puzzle(puzzle):
        return len(puzzle) == 7 and puzzle.isalpha() and len(set(puzzle)) == 7

    def read_dictionary():
        with open(DICTIONARY_FILE, 'r') as file:
            return [line.strip() for line in file]

    def is_valid_word(word, beehive_letters, center_letter):
        return (
            len(word) >= 4 and 
            all(letter in beehive_letters for letter in word) and 
            center_letter in word
        )

    def is_pangram(word, beehive_letters):
        return all(letter in word for letter in beehive_letters)

    def calculate_score(word, beehive_letters):
        score = len(word)
        if is_pangram(word, beehive_letters):
            score += 7  # Bonus for pangram
        return score

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)
    sbg.add_field("Word", word_action)

# Startup code
if __name__ == "__main__":
    spelling_bee()