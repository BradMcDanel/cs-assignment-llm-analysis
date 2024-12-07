from SpellingBeeGraphics import SpellingBeeGraphics

# Constants
DICTIONARY_FILE = "EnglishWords.txt"

def load_dictionary():
    with open(DICTIONARY_FILE, 'r') as f:
        return set(word.strip().lower() for word in f)

def is_valid_puzzle(letters):
    return (len(letters) == 7 and
            letters.isalpha() and
            len(set(letters)) == 7)

def word_is_valid(word, center, letters):
    return (len(word) >= 4 and
            center in word and
            all(letter in letters for letter in word))

def calculate_score(word, letters):
    if len(word) == 4:
        return 1
    score = len(word)
    if set(word) == set(letters):
        score += 7  # Pangram bonus
    return score

def spelling_bee():
    sbg = SpellingBeeGraphics()
    dictionary = load_dictionary()
    puzzle_letters = ""
    found_words = set()
    total_score = 0

    def puzzle_action(s):
        nonlocal puzzle_letters
        s = s.lower()
        if is_valid_puzzle(s):
            puzzle_letters = s
            sbg.set_beehive_letters(s)
            sbg.show_message("Puzzle set successfully!")
        else:
            sbg.show_message("Invalid puzzle. Please enter 7 unique letters.", "Red")

    def solve_action(s):
        if not puzzle_letters:
            sbg.show_message("Please set a valid puzzle first.", "Red")
            return
        
        sbg.clear_word_list()
        center = puzzle_letters[0]
        valid_words = [word for word in dictionary if word_is_valid(word, center, puzzle_letters)]
        
        total_score = 0
        word_count = 0
        for word in valid_words:
            score = calculate_score(word, puzzle_letters)
            total_score += score
            word_count += 1
            color = "Blue" if set(word) == set(puzzle_letters) else "Black"
            sbg.add_word(f"{word} ({score})", color)
        
        sbg.show_message(f"Found {word_count} words. Total score: {total_score}")

    def word_action(s):
        if not puzzle_letters:
            sbg.show_message("Please set a valid puzzle first.", "Red")
            return
        
        word = s.lower()
        center = puzzle_letters[0]
        
        if word in found_words:
            sbg.show_message("Word already found!", "Red")
        elif word not in dictionary:
            sbg.show_message("Word not in dictionary.", "Red")
        elif not word_is_valid(word, center, puzzle_letters):
            if len(word) < 4:
                sbg.show_message("Word too short.", "Red")
            elif center not in word:
                sbg.show_message("Word doesn't contain center letter.", "Red")
            else:
                sbg.show_message("Word contains invalid letters.", "Red")
        else:
            score = calculate_score(word, puzzle_letters)
            found_words.add(word)
            color = "Blue" if set(word) == set(puzzle_letters) else "Black"
            sbg.add_word(f"{word} ({score})", color)
            
            nonlocal total_score
            total_score += score
            sbg.show_message(f"Good! {len(found_words)} words. Score: {total_score}")
            sbg.set_field("Word", "")  # Clear the word field

    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)
    sbg.add_field("Word", word_action)

if __name__ == "__main__":
    spelling_bee()