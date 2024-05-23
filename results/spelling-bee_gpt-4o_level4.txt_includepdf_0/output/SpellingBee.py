from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

def spelling_bee():
    sbg = SpellingBeeGraphics()

    def puzzle_action(s):
        s = s.strip().upper()
        if len(s) != 7:
            sbg.show_message("Puzzle must contain exactly seven characters.", "Red")
            return
        if not s.isalpha():
            sbg.show_message("Puzzle must contain only letters.", "Red")
            return
        if len(set(s)) != 7:
            sbg.show_message("Puzzle must not contain repeated characters.", "Red")
            return
        sbg.set_beehive_letters(s)
        sbg.show_message("")

    def solve_action(s):
        beehive_letters = sbg.get_beehive_letters()
        if not beehive_letters:
            sbg.show_message("No valid puzzle set.", "Red")
            return
        
        center_letter = beehive_letters[0]
        valid_words = []
        with open(DICTIONARY_FILE, "r") as file:
            for word in file:
                word = word.strip()
                if len(word) < 4:
                    continue
                if center_letter not in word:
                    continue
                if all(char in beehive_letters for char in word.upper()):
                    valid_words.append(word)
        
        sbg.clear_word_list()
        for word in valid_words:
            color = "Blue" if len(set(word.upper())) == 7 else "Black"
            sbg.add_word(word, color)

        total_score = sum(1 if len(word) == 4 else len(word) + (7 if len(set(word.upper())) == 7 else 0) for word in valid_words)
        sbg.show_message(f"Total Words: {len(valid_words)}, Total Score: {total_score}")

    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

if __name__ == "__main__":
    spelling_bee()