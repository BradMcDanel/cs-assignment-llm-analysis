from SpellingBeeGraphics import SpellingBeeGraphics

def solve_action(s):
    dictionary = read_dictionary(DICTIONARY_FILE)
    beehive = sbg.get_beehive_letters()
    total_score = 0
    word_count = 0
    for word in dictionary:
        if is_valid_word(word, beehive):
            word_score = len(word) if len(word) < 7 else 7
            if len(word) == 7:
                word_score += 7
                sbg.add_word(word, "Blue")
            sbg.add_word(word + " (" + str(word_score) + ")")
            total_score += word_score
            word_count += 1
    sbg.show_message("Found " + str(word_count) + " words. Total score: " + str(total_score))

if __name__ == "__main__":
    solve_action()