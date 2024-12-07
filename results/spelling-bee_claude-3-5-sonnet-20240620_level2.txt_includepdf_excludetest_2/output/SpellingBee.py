from SpellingBeeGraphics import SpellingBeeGraphics

DICTIONARY_FILE = "EnglishWords.txt"

def spelling_bee():
    def read_dictionary():
        with open(DICTIONARY_FILE, 'r') as f:
            return set(word.strip().lower() for word in f)

    def is_valid_puzzle(letters):
        return (len(letters) == 7 and
                letters.isalpha() and
                len(set(letters)) == 7)

    def is_valid_word(word, center, letters):
        return (len(word) >= 4 and
                center in word and
                all(letter in letters for letter in word))

    def calculate_score(word, letters):
        score = len(word)
        if score == 4:
            score = 1
        if set(word) == set(letters):
            score += 7
        return score

    def puzzle_action(s):
        if is_valid_puzzle(s):
            sbg.set_beehive_letters(s.upper())
            sbg.show_message("Puzzle set successfully!")
        else:
            sbg.show_message("Invalid puzzle! Use 7 unique letters.", "Red")

    def solve_action(s):
        letters = sbg.get_beehive_letters().lower()
        center = letters[0]
        words = read_dictionary()
        valid_words = [word for word in words if is_valid_word(word, center, letters)]
        
        sbg.clear_word_list()
        total_score = 0
        for word in sorted(valid_words):
            score = calculate_score(word, letters)
            total_score += score
            color = "Blue" if set(word) == set(letters) else "Black"
            sbg.add_word(f"{word} ({score})", color)
        
        msg = f"Found {len(valid_words)} words. Total score: {total_score}"
        sbg.show_message(msg)

    def word_action(s):
        letters = sbg.get_beehive_letters().lower()
        center = letters[0]
        word = s.lower()
        
        if word not in read_dictionary():
            sbg.show_message("Word not in dictionary.", "Red")
        elif len(word) < 4:
            sbg.show_message("Word must be at least 4 letters long.", "Red")
        elif center not in word:
            sbg.show_message(f"Word must contain the center letter '{center.upper()}'.", "Red")
        elif not all(letter in letters for letter in word):
            sbg.show_message("Word contains invalid letters.", "Red")
        elif sbg.get_field("Word") in [item.split()[0] for item in sbg._wordlist]:
            sbg.show_message("Word already found.", "Red")
        else:
            score = calculate_score(word, letters)
            color = "Blue" if set(word) == set(letters) else "Black"
            sbg.add_word(f"{word} ({score})", color)
            sbg.set_field("Word", "")
            
            total_score = sum(int(item.split("(")[1].split(")")[0]) for item in sbg._wordlist)
            msg = f"Found {len(sbg._wordlist)} words. Total score: {total_score}"
            sbg.show_message(msg)

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)
    sbg.add_field("Word", word_action)

if __name__ == "__main__":
    spelling_bee()