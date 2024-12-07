def apply_permutation(index, permutation, offset):
    shifted_index = (index + offset) % 26
    new_char = permutation[shifted_index]
    new_index = (ALPHABET.index(new_char) - offset) % 26
    return new_index

# Update EnigmaModel.py

    def key_pressed(self, letter):
        self._key_states[letter] = True
        index = ALPHABET.index(letter)
        # Encrypt through the fast rotor only for now
        new_index = apply_permutation(index, self._rotors[2].get_permutation(), self._rotors[2].get_offset())
        new_letter = ALPHABET[new_index]
        self._lamp_states = {letter: False for letter in ALPHABET}
        self._lamp_states[new_letter] = True
        self.update()

    def is_lamp_on(self, letter):
        return self._lamp_states.get(letter, False)