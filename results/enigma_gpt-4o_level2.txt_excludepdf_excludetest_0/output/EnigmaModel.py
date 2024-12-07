class EnigmaModel:
    # ... (class code remains unchanged) ...

    def key_pressed(self, letter):
        self._key_state[letter] = True

        # Advance the fast rotor and handle carry
        carry = self.rotors[0].advance()
        if carry:
            carry = self.rotors[1].advance()
            if carry:
                self.rotors[2].advance()

        index = ord(letter) - ord('A')
        for rotor in self.rotors:
            index = apply_permutation(index, rotor.get_permutation(), rotor.get_offset())

        index = apply_permutation(index, REFLECTOR_PERMUTATION, 0)

        for rotor in reversed(self.rotors):
            index = apply_permutation(index, rotor.get_inverse_permutation(), rotor.get_offset())

        new_letter = chr(index + ord('A'))
        self._lamp_state[new_letter] = True
        self.update()

    # ... (other methods remain unchanged) ...