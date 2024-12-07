class EnigmaModel:
    # Initialization and other methods remain unchanged

    def key_pressed(self, letter):
        # Advance the fast rotor first
        carry = self.rotors[0].advance()
        # Check if medium rotor needs to advance
        if carry:
            carry = self.rotors[1].advance()
        # Check if slow rotor needs to advance
        if carry:
            self.rotors[2].advance()

        # Perform encryption as before
        index = ord(letter) - ord('A')
        for rotor in self.rotors:
            index = apply_permutation(index, rotor.get_permutation(), rotor.get_offset())
        index = apply_permutation(index, REFLECTOR_PERMUTATION, 0)
        for rotor in reversed(self.rotors):
            index = apply_permutation(index, rotor.inverse_permutation, rotor.get_offset())
        
        encrypted_letter = chr(index + ord('A'))
        self._lamp_states[encrypted_letter] = True
        self.update()

    # Other methods remain unchanged