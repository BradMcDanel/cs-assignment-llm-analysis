# Modify the advance method in EnigmaRotor class

def advance(self):
    self._offset = (self._offset + 1) % 26
    return self._offset == 0  # Return True if a carry occurs

# Modify key_pressed method in EnigmaModel class

def key_pressed(self, letter):
    # Advance the fast rotor and propagate carry
    carry = self._rotors[2].advance()
    if carry:
        carry = self._rotors[1].advance()
        if carry:
            self._rotors[0].advance()
    # Rest of the key_pressed function remains unchanged...