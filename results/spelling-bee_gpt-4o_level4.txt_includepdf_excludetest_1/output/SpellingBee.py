from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

def spelling_bee():
    def puzzle_action(s):
        # Check if the input is valid for the puzzle
        if len(s) != 7 or not s.isalpha() or len(set(s)) != 7:
            sbg.show_message("The puzzle must contain exactly seven unique letters.", "Red")
        else:
            sbg.set_beehive_letters(s.upper())
            sbg.show_message("Puzzle set!", "Green")
    
    def solve_action(s):
        sbg.clear_word_list()
        letters = sbg.get_beehive_letters().lower()
        center_letter = letters[0]
        valid_words = []
        with open(DICTIONARY_FILE, 'r') as file:
            dictionary = file.read().splitlines()
        
        for word in dictionary:
            if (len(word) >= 4 and
                all(c in letters for c in word) and
                center_letter in word):
                valid_words.append(word)

        total_score = 0
        for word in valid_words:
            score = len(word) if len(word) > 4 else 1
            if all(l in word for l in letters):
                score += 7
                sbg.add_word(word, "Blue")
            else:
                sbg.add_word(word)
            total_score += score
        
        sbg.show_message(f"Found {len(valid_words)} words. Total score: {total_score}.", "Green")

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

# Startup code
if __name__ == "__main__":
    spelling_bee()