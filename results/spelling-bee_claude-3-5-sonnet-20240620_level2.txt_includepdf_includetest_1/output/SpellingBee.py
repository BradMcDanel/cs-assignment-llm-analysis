from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"
MIN_WORD_LENGTH = 4

class SpellingBee:
    def __init__(self):
        self.sbg = SpellingBeeGraphics()
        self.sbg.add_field("Puzzle", self.puzzle_action)
        self.sbg.add_field("Word", self.word_action)
        self.sbg.add_button("Solve", self.solve_action)
        self.dictionary = self.load_dictionary()
        self.puzzle_letters = ""
        self.found_words = set()
        self.total_score = 0

    def load_dictionary(self):
        with open(DICTIONARY_FILE, 'r') as file:
            return set(word.strip().lower() for word in file)

    def is_valid_puzzle(self, letters):
        return (len(letters) == 7 and
                letters.isalpha() and
                len(set(letters)) == 7)

    def puzzle_action(self, letters):
        letters = letters.upper()
        if self.is_valid_puzzle(letters):
            self.puzzle_letters = letters
            self.sbg.set_beehive_letters(letters)
            self.sbg.show_message("Puzzle set successfully!")
            self.found_words.clear()
            self.total_score = 0
        else:
            self.sbg.show_message("Invalid puzzle. Please enter 7 unique letters.", "Red")

    def is_valid_word(self, word):
        if len(word) < MIN_WORD_LENGTH:
            return False
        if not set(word).issubset(set(self.puzzle_letters.lower())):
            return False
        if self.puzzle_letters[0].lower() not in word:
            return False
        return word in self.dictionary

    def calculate_score(self, word):
        score = len(word)
        if score == 4:
            score = 1
        if set(word) == set(self.puzzle_letters.lower()):
            score += 7  # Pangram bonus
        return score

    def word_action(self, word):
        word = word.lower()
        if word in self.found_words:
            self.sbg.show_message("Word already found!", "Red")
        elif self.is_valid_word(word):
            score = self.calculate_score(word)
            self.found_words.add(word)
            self.total_score += score
            color = "Blue" if len(set(word)) == 7 else "Black"
            self.sbg.add_word(f"{word} ({score})", color)
            self.sbg.set_field("Word", "")
            self.update_score_message()
        else:
            self.sbg.show_message("Invalid word.", "Red")

    def solve_action(self, _):
        if not self.puzzle_letters:
            self.sbg.show_message("Please set a puzzle first.", "Red")
            return

        self.sbg.clear_word_list()
        for word in self.dictionary:
            if self.is_valid_word(word) and word not in self.found_words:
                score = self.calculate_score(word)
                self.total_score += score
                self.found_words.add(word)
                color = "Blue" if len(set(word)) == 7 else "Black"
                self.sbg.add_word(f"{word} ({score})", color)

        self.update_score_message()

    def update_score_message(self):
        message = f"Words: {len(self.found_words)}, Score: {self.total_score}"
        self.sbg.show_message(message)

def spelling_bee():
    SpellingBee()

if __name__ == "__main__":
    spelling_bee()