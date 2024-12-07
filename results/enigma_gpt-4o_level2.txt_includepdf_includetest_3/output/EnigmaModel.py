class EnigmaModel:

    # Other methods remain unchanged

    def key_pressed(self, letter):
        """Handles the event when a key is pressed."""
        self._key_states[letter] = True

        # Advance the fast rotor and carry if needed
        if self._rotors[2].advance():
            if self._rotors[1].advance():
                self._rotors[0].advance()

        # Encrypt the letter
        index = ALPHABET.index(letter)
        for rotor in reversed(self._rotors):
            index = apply_permutation(index, rotor.get_permutation(), rotor.get_offset())
        index = ALPHABET.index(REFLECTOR_PERMUTATION[index])
        for rotor in self._rotors:
            index = apply_permutation(index, rotor.get_permutation(), rotor.get_offset())

        self._lamp_state = ALPHABET[index]
        self.update()