class EnigmaRotor:
    ...
    def advance(self):
        self._offset = (self._offset + 1) % 26
        return self._offset == 0  # Return True if it wraps around

### EnigmaModel.py ###
def key_pressed(self, letter):
    # Advance rotors accordingly
    carry = self._rotors[0].advance()
    if carry:
        carry = self._rotors[1].advance()
        if carry:
            self._rotors[2].advance()

    self._key_states[letter] = True
    index = ord(letter) - ord('A')
    
    # Encryption logic as before...