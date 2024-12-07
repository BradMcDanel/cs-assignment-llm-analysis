class EnigmaModel:

    # ...

    def key_pressed(self, letter):
        self._key_states[letter] = True
        self._advance_rotors()
        index = ord(letter) - ord('A')
        index = self._apply_rotors(index)
        encrypted_letter = chr(index + ord('A'))
        self._lamp_states[encrypted_letter] = True
        self.update()

    def _advance_rotors(self):
        carry = self._rotors[2].advance()
        if carry:
            carry = self._rotors[1].advance()
            if carry:
                self._rotors[0].advance()

    def _apply_rotors(self, index):
        # Right to left through rotors
        for rotor in reversed(self._rotors):
            index = apply_permutation(index, rotor.get_permutation(), rotor.get_offset())
        # Reflector
        index = apply_permutation(index, REFLECTOR_PERMUTATION, 0)
        # Left to right through rotors
        for rotor in self._rotors:
            index = apply_permutation(index, rotor.get_permutation(), rotor.get_offset())
        return index