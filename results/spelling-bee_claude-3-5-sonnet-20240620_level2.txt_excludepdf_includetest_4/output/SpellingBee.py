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
        with open(DICTIONARY_FILE) as f:
            return set(word.strip().lower() for word in f)
        
    def puzzle_action(self, puzzle):
        if self.is_valid_puzzle(puzzle):
            self.puzzle_letters = puzzle.upper()
            self.sbg.set_beehive_letters(self.puzzle_letters)
            self.sbg.show_message("Valid puzzle entered!")
            self.found_words.clear()
            self.total_score = 0
        else:
            self.sbg.show_message("Invalid puzzle. Must be 7 unique letters.", "Red")
            
    def is_valid_puzzle(self, puzzle):
        return (len(puzzle) == 7 and 
                puzzle.isalpha() and
                len(set(puzzle.lower())) == 7)
    
    def word_action(self, word):
        word = word.lower()
        if self.is_valid_word(word):
            if word not in self.found_words:
                self.found_words.add(word)
                score = self.score_word(word)
                self.total_score += score
                color = "Blue" if self.is_pangram(word) else "Black"
                self.sbg.add_word(f"{word} ({score})", color)
                self.update_score_display()
                self.sbg.set_field("Word", "")
            else:
                self.sbg.show_message("Word already found!", "Red")
        else:
            self.sbg.show_message(self.get_invalid_word_message(word), "Red")
        
    def is_valid_word(self, word):
        return (word in self.dictionary and
                len(word) >= MIN_WORD_LENGTH and
                set(word).issubset(set(self.puzzle_letters.lower())) and
                self.puzzle_letters[0].lower() in word)
    
    def get_invalid_word_message(self, word):
        if word not in self.dictionary:
            return "Word not in dictionary"
        if len(word) < MIN_WORD_LENGTH:
            return f"Word must be at least {MIN_WORD_LENGTH} letters long"
        if not set(word).issubset(set(self.puzzle_letters.lower())):
            return "Word contains letters not in puzzle"
        if self.puzzle_letters[0].lower() not in word:
            return "Word must contain center letter"
        return "Invalid word"
    
    def score_word(self, word):
        base_score = len(word) if len(word) > 4 else 1
        pangram_bonus = 7 if self.is_pangram(word) else 0
        return base_score + pangram_bonus
    
    def is_pangram(self, word):
        return set(word) == set(self.puzzle_letters.lower())
    
    def update_score_display(self):
        msg = f"Words: {len(self.found_words)} | Score: {self.total_score}"
        self.sbg.show_message(msg)
    
    def solve_action(self, _):
        self.sbg.clear_word_list()
        for word in self.dictionary:
            if self.is_valid_word(word):
                score = self.score_word(word)
                color = "Blue" if self.is_pangram(word) else "Black"
                self.sbg.add_word(f"{word} ({score})", color)
        self.update_score_display()

def spelling_bee():
    SpellingBee()

if __name__ == "__main__":
    spelling_bee()