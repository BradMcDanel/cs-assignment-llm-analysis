from SpellingBeeGraphics import SpellingBeeGraphics

DICTIONARY_FILE = "EnglishWords.txt"

def spelling_bee():
    def puzzle_action(s):
        entered_letters = sbg.get_field("Puzzle")
        if len(entered_letters) != 7 or not entered_letters.isalpha() or len(set(entered_letters)) != 7:
            sbg.show_message("Invalid puzzle format. Puzzle must have exactly 7 unique letters.", "Red")
        else:
            sbg.set_beehive_letters(entered_letters)

    def solve_action(s):
        sbg.clear_word_list()
        puzzle_letters = sbg.get_beehive_letters()
        # Implement word checking logic based on puzzle_letters and DICTIONARY_FILE
        # Add valid words to the word list using sbg.add_word(word, color)

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

if __name__ == "__main__":
    spelling_bee()