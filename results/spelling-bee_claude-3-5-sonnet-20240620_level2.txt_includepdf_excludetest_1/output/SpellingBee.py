from SpellingBeeGraphics import SpellingBeeGraphics

DICTIONARY_FILE = "EnglishWords.txt"

def spelling_bee():
    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)
    sbg.add_field("Word", word_action)
    
    global dictionary, found_words, total_score
    dictionary = load_dictionary()
    found_words = set()
    total_score = 0

def load_dictionary():
    with open(DICTIONARY_FILE, 'r') as f:
        return set(word.strip().lower() for word in f)

def is_valid_puzzle(letters):
    return (len(letters) == 7 and 
            letters.isalpha() and
            len(set(letters)) == 7)

def puzzle_action(letters):
    if is_valid_puzzle(letters):
        sbg.set_beehive_letters(letters)
        sbg.show_message("Puzzle set! Enter words or click Solve.")
    else:
        sbg.show_message("Invalid puzzle. Must be 7 unique letters.", "Red")

def is_valid_word(word, puzzle):
    center = puzzle[0].lower()
    puzzle = set(puzzle.lower())
    return (len(word) >= 4 and
            center in word and
            set(word).issubset(puzzle) and
            word in dictionary)

def calculate_score(word):
    score = len(word)
    if score == 4:
        score = 1
    if len(set(word)) == 7:
        score += 7
    return score

def solve_action(s):
    puzzle = sbg.get_beehive_letters()
    if not puzzle:
        sbg.show_message("Set a puzzle first!", "Red")
        return
    
    sbg.clear_word_list()
    words = [word for word in dictionary if is_valid_word(word, puzzle)]
    words.sort()
    
    global total_score
    total_score = 0
    for word in words:
        score = calculate_score(word)
        total_score += score
        color = "Blue" if len(set(word)) == 7 else "Black"
        sbg.add_word(f"{word} ({score})", color)
    
    sbg.show_message(f"Found {len(words)} words. Total score: {total_score}")

def word_action(word):
    word = word.lower()
    puzzle = sbg.get_beehive_letters()
    
    if not puzzle:
        sbg.show_message("Set a puzzle first!", "Red")
    elif word in found_words:
        sbg.show_message("Word already found!", "Red")
    elif not is_valid_word(word, puzzle):
        if len(word) < 4:
            sbg.show_message("Word must be at least 4 letters long.", "Red")
        elif puzzle[0].lower() not in word:
            sbg.show_message("Word must contain the center letter.", "Red")
        elif not set(word).issubset(set(puzzle.lower())):
            sbg.show_message("Word contains invalid letters.", "Red")
        else:
            sbg.show_message("Word not in dictionary.", "Red")
    else:
        score = calculate_score(word)
        global total_score
        total_score += score
        found_words.add(word)
        color = "Blue" if len(set(word)) == 7 else "Black"
        sbg.add_word(f"{word} ({score})", color)
        sbg.set_field("Word", "")
        sbg.show_message(f"Good! {len(found_words)} words. Score: {total_score}")

if __name__ == "__main__":
    spelling_bee()