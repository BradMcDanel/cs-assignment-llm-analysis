from SpellingBeeGraphics import SpellingBeeGraphics

def check_user_word(word, puzzle, found_words):
    if word in found_words:
        return False, "Word already found"
    if word not in dictionary:
        return False, "Word not in dictionary"
    if len(word) < 4:
        return False, "Word must be at least 4 letters long"
    if puzzle[0] not in word:
        return False, "Word must contain the center letter"
    if not all(letter in puzzle for letter in word):
        return False, "Word includes letters not in the beehive"
    
    return True, ""

def user_action(s):
    user_word = sbg.get_field("Word").lower()
    puzzle = sbg.get_beehive_letters()
    valid_word, message = check_user_word(user_word, puzzle, found_words)

    if valid_word:
        score = calculate_score(user_word)
        sbg.add_word(f"{user_word} ({score})")
        found_words.add(user_word)
        total_score += score
        word_count += 1
        sbg.show_message(f"Total Words Found: {word_count}, Total Score: {total_score}")
        sbg.set_field("Word", "")
    else:
        sbg.show_message(message, "Red")

sbg = SpellingBeeGraphics()
sbg.add_field("Puzzle", lambda s: sbg.set_beehive_letters(s.upper()))
sbg.add_button("Solve", solve_action)
sbg.add_field("Word", user_action)