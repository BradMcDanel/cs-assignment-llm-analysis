def spelling_bee():

    # ... (previous code)

    found_words = set()

    def word_action(word):
        word = word.lower()
        if word in found_words:
            sbg.show_message("Word already found.", "Red")
            return
        beehive_letters = sbg.get_beehive_letters().lower()
        center_letter = beehive_letters[0]
        dictionary = load_dictionary()

        if word not in dictionary:
            sbg.show_message("Word not in dictionary.", "Red")
        elif not is_valid_word(word, beehive_letters, center_letter):
            sbg.show_message("Word not valid.", "Red")
        else:
            is_pangram = all(char in word for char in beehive_letters)
            score = calculate_score(word, is_pangram)
            color = "Blue" if is_pangram else "Black"
            sbg.add_word(f"{word} ({score})", color)
            found_words.add(word)
            sbg.show_message(f"Found {len(found_words)} words. Total score: {sum(calculate_score(w, all(c in w for c in beehive_letters)) for w in found_words)}.", "Green")
            sbg.set_field("Word", "")

    sbg.add_field("Word", word_action)

    # ... (rest of the code)