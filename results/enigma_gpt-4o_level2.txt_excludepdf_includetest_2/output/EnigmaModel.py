# Continue from the previous code

# Update advance method to return a carry flag
    def advance(self):
        self._offset = (self._offset + 1) % 26
        return self._offset == 0

# Update key_pressed method in EnigmaModel
    def key_pressed(self, letter):
        self._key_states[letter] = True
        # Advance the fast rotor
        carry = self._rotors[0].advance()

        # Propagate the carry if necessary
        for i in range(1, len(self._rotors)):
            if carry:
                carry = self._rotors[i].advance()
            else:
                break

        index = ord(letter) - 65

        # Forward path through rotors
        for rotor in self._rotors:
            index = apply_permutation(index, rotor.get_permutation(), rotor.get_offset())

        # Reflector
        index = apply_permutation(index, REFLECTOR_PERMUTATION, 0)

        # Backward path through rotors
        for rotor in reversed(self._rotors):
            index = apply_permutation(index, rotor.get_inverse_permutation(), rotor.get_offset())

        # Light up the corresponding lamp
        self._key_states[chr(65 + index)] = True
        self.update()