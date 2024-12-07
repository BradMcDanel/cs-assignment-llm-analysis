class EnigmaModel:
    ...

    def key_pressed(self, letter):
        # Advance rotors before encryption
        carry = self.rotors[0].advance()
        if carry:
            carry = self.rotors[1].advance()
            if carry:
                self.rotors[2].advance()

        letter_index = ord(letter) - ord('A')

        # Forward pass through rotors
        for rotor in self.rotors:
            letter_index = apply_permutation(letter_index, rotor.get_permutation(), rotor.get_offset())
        
        # Reflector
        reflector = ROTOR_PERMUTATIONS[-1]
        letter_index = apply_permutation(letter_index, reflector, 0)

        # Backward pass through rotors
        for rotor in reversed(self.rotors):
            letter_index = apply_permutation(letter_index, rotor.inverse_permutation, rotor.get_offset())

        new_letter = chr(letter_index + ord('A'))
        self._key_state[new_letter] = True
        self.update()