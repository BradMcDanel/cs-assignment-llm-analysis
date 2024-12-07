def key_pressed(self, letter):
    self._key_state[letter] = True
    
    # Advance rotors
    carry = self._rotors[0].advance()
    if carry:
        carry = self._rotors[1].advance()
        if carry:
            self._rotors[2].advance()
    
    # Encryption logic remains the same
    letter_index = ord(letter) - 65
    for rotor in self._rotors:
        letter_index = apply_permutation(letter_index, rotor.get_permutation(), rotor.get_offset())
    reflected_index = apply_permutation(letter_index, REFLECTOR_PERMUTATION, 0)
    for rotor in reversed(self._rotors):
        reflected_index = apply_permutation(reflected_index, invert_key(rotor.get_permutation()), rotor.get_offset())
    
    encrypted_letter = chr(65 + reflected_index)
    self.update()