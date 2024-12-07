from EnigmaConstants import REFLECTOR_PERMUTATION

class EnigmaModel:
    # ... existing code ...

    def key_pressed(self, letter):
        self._key_states[letter] = True
        index = ord(letter) - ord('A')
        for rotor in reversed(self._rotors):  # Right to left
            index = apply_permutation(index, rotor.get_permutation(), rotor.get_offset())
        index = apply_permutation(index, REFLECTOR_PERMUTATION, 0)
        for rotor in self._rotors:  # Left to right
            index = apply_permutation(index, rotor.get_permutation(), rotor.get_offset())
        encrypted_letter = chr(index + ord('A'))
        self._lamp_states = {l: l == encrypted_letter for l in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
        self.update()