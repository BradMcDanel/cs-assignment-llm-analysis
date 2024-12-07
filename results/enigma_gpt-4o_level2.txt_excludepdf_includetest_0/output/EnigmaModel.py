class EnigmaModel:
    # Continue from previous code

    def key_pressed(self, letter):
        self._key_state[letter] = True

        # Advance rotors
        carry = True
        for rotor in reversed(self._rotors):
            if carry:
                carry = rotor.advance()
            else:
                break

        index = ord(letter) - ord('A')

        # Right to left through rotors
        for rotor in reversed(self._rotors):
            index = apply_permutation(index, rotor.get_permutation(), rotor.get_offset())

        # Reflector
        index = apply_permutation(index, REFLECTOR_PERMUTATION, 0)

        # Left to right through rotors
        for rotor in self._rotors:
            index = apply_permutation(index, rotor.get_inverse_permutation(), rotor.get_offset())

        encrypted_letter = chr(index + ord('A'))
        self._lamp_state[encrypted_letter] = True
        self.update()

    # The rest of the code remains the same