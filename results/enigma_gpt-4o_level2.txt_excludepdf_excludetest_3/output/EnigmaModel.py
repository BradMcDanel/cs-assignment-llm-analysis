# Continuing from the previous implementation...

def key_pressed(self, letter):
    # Advance fast rotor
    carry = self.rotors[0].advance()

    # Handle carry to medium rotor
    if carry:
        carry = self.rotors[1].advance()

    # Handle carry to slow rotor
    if carry:
        self.rotors[2].advance()

    # Encryption process as before...
    self._key_states[letter] = True
    index = ord(letter) - ord('A')

    # Pass through all rotors right to left
    for rotor in self.rotors:
        index = apply_permutation(index, rotor.get_permutation(), rotor.get_offset())

    # Reflect
    index = apply_permutation(index, REFLECTOR_PERMUTATION, 0)

    # Pass through all rotors left to right (inverse)
    for rotor in reversed(self.rotors):
        index = apply_inverse_permutation(index, rotor.get_permutation(), rotor.get_offset())

    encrypted_letter = chr((index + ord('A')) % 26)
    self._key_states[encrypted_letter] = True
    self.update()

def enigma():
    """Runs the Enigma simulator."""
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

# Startup code
if __name__ == "__main__":
    enigma()