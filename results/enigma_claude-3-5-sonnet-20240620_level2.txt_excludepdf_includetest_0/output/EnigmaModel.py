# ... (previous code remains the same)

class EnigmaModel:

    # ... (previous methods remain the same)

    def key_pressed(self, letter):
        self._key_state[letter] = True
        
        # Advance rotors
        if self._rotors[2].advance():
            if self._rotors[1].advance():
                self._rotors[0].advance()
        
        # Implement full encryption path
        index = ord(letter) - ord('A')
        
        # Right to left through rotors
        for rotor in reversed(self._rotors):
            index = apply_permutation(index, rotor.get_permutation(), rotor.get_offset())
        
        # Through reflector
        index = apply_permutation(index, self._reflector, 0)
        
        # Left to right through rotors
        for rotor in self._rotors:
            index = apply_permutation(index, rotor.get_inverse_permutation(), rotor.get_offset())
        
        encrypted_letter = chr(index + ord('A'))
        self._lamp_state[encrypted_letter] = True
        self.update()

    # ... (rest of the file remains the same)

class EnigmaRotor:
    # ... (previous methods remain the same)

    def advance(self):
        self._offset = (self._offset + 1) % 26
        return self._offset == 0  # Return True if we've made a full revolution