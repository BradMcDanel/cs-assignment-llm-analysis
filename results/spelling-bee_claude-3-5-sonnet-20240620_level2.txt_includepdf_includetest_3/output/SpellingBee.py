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
        self.found_words = set()
        self.total_score = 0
        self.word_count = 0

    def load_dictionary(self):
        with open(DICTIONARY_FILE, 'r') as f:
            return set(word.strip().lower() for word in f)

    def is_valid_puzzle(self, puzzle):
        return (len(puzzle) == 7 and
                puzzle.isalpha() and
                len(set(puzzle)) == 7)

    def puzzle_action(self, puzzle):
        puzzle = puzzle.upper()
        if self.is_valid_puzzle(puzzle):
            self.sbg.set_beehive_letters(puzzle)
            self.sbg.show_message(f"Puzzle set to {puzzle}")
            self.found_words.clear()
            self.total_score = 0
            self.word_count = 0
            self.sbg.clear_word_list()
        else:
            self.sbg.show_message("Invalid puzzle. Must be 7 unique letters.", "Red")

    def is_valid_word(self, word):
        puzzle = self.sbg.get_beehive_letters().lower()
        return (len(word) >= MIN_WORD_LENGTH and
                set(word).issubset(set(puzzle)) and
                puzzle[0] in word and
                word in self.dictionary and
                word not in self.found_words)

    def calculate_score(self, word):
        score = len(word)
        if len(set(word)) == 7:
            score += 7  # Pangram bonus
        return max(score, 1)  # Minimum score is 1

    def word_action(self, word):
        word = word.lower()
        if self.is_valid_word(word):
            score = self.calculate_score(word)
            self.found_words.add(word)
            self.total_score += score
            self.word_count += 1
            color = "Blue" if len(set(word)) == 7 else "Black"
            self.sbg.add_word(f"{word} ({score})", color)
            self.sbg.set_field("Word", "")
            self.update_score_message()
        else:
            if word in self.found_words:
                message = "Word already found"
            elif len(word) < MIN_WORD_LENGTH:
                message = f"Word must be at least {MIN_WORD_LENGTH} letters long"
            elif self.sbg.get_beehive_letters()[0].lower() not in word:
                message = "Word must contain the center letter"
            elif not set(word).issubset(set(self.sbg.get_beehive_letters().lower())):
                message = "Word contains invalid letters"
            else:
                message = "Word not in dictionary"
            self.sbg.show_message(message, "Red")

    def solve_action(self, _):
        puzzle = self.sbg.get_beehive_letters().lower()
        for word in self.dictionary:
            if self.is_valid_word(word):
                if word not in self.found_words:
                    score = self.calculate_score(word)
                    self.found_words.add(word)
                    self.total_score += score
                    self.word_count += 1
                    color = "Blue" if len(set(word)) == 7 else "Black"
                    self.sbg.add_word(f"{word} ({score})", color)
        self.update_score_message()

    def update_score_message(self):
        self.sbg.show_message(f"Words: {self.word_count}, Score: {self.total_score}")

def spelling_bee():
    game = SpellingBee()

if __name__ == "__main__":
    spelling_bee()