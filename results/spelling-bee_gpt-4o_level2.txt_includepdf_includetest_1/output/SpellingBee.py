from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

def spelling_bee():
    found_words = set()

    def puzzle_action(s):
        if len(s) != 7 or not s.isalpha() or len(set(s.lower())) != 7:
            sbg.show_message("Puzzle must contain exactly 7 unique letters.", "Red")
            return
        sbg.set_beehive_letters(s.upper())
        sbg.show_message("Beehive updated successfully.", "Green")

    def solve_action(s):
        sbg.clear_word_list()
        beehive_letters = sbg.get_beehive_letters().lower()
        center_letter = beehive_letters[0]
        total_score = 0
        total_words = 0

        with open(DICTIONARY_FILE, 'r') as file:
            for word in file:
                word = word.strip()
                if len(word) >= 4 and center_letter in word and all(c in beehive_letters for c in word):
                    score = len(word) + (7 if len(set(word)) == 7 else 0)
                    total_score += score
                    total_words += 1
                    sbg.add_word(f"{word} ({score})", "Blue" if len(set(word)) == 7 else "Black")

        sbg.show_message(f"Total words: {total_words}, Total score: {total_score}", "Green")

    def word_action(s):
        word = s.strip().lower()
        sbg.set_field("Word", "")
        if word in found_words:
            sbg.show_message(f"You have already found the word '{word}'.", "Red")
            return
        
        beehive_letters = sbg.get_beehive_letters().lower()
        center_letter = beehive_letters[0]

        with open(DICTIONARY_FILE, 'r') as file:
            if word in file.read().splitlines():
                if len(word) >= 4 and center_letter in word and all(c in beehive_letters for c in word):
                    found_words.add(word)
                    score = len(word) + (7 if len(set(word)) == 7 else 0)
                    sbg.add_word(f"{word} ({score})", "Blue" if len(set(word)) == 7 else "Black")
                    sbg.show_message(f"Word '{word}' accepted. Score: {score}.", "Green")
                    return

        sbg.show_message(f"Word '{word}' is invalid.", "Red")

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_field("Word", word_action)
    sbg.add_button("Solve", solve_action)

# Startup code
if __name__ == "__main__":
    spelling_bee()