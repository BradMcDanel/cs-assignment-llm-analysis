from EnigmaView import EnigmaView
from EnigmaConstants import ROTOR_PERMUTATIONS, REFLECTOR_PERMUTATION, ALPHABET

class EnigmaRotor:
    def __init__(self, permutation):
        self._permutation = permutation
        self._inverse_permutation = self._invert_permutation(permutation)
        self._offset = 0

    def get_offset(self):
        return self._offset

    def get_permutation(self):
        return self._permutation

    def get_inverse_permutation(self):
        return self._inverse_permutation

    def advance(self):
        self._offset = (self._offset + 1) % 26
        return self._offset == 0  # Return True if it wraps around

    def _invert_permutation(self, permutation):
        inverse = [''] * 26
        for i, char in enumerate(permutation):
            index = ord(char) - ord('A')
            inverse[index] = ALPHABET[i]
        return ''.join(inverse)

class EnigmaModel:

    def __init__(self):
        """Creates a new EnigmaModel with no views."""
        self._views = []
        self._key_state = {letter: False for letter in ALPHABET}
        self._lamp_state = {letter: False for letter in ALPHABET}
        self._rotors = [EnigmaRotor(ROTOR_PERMUTATIONS[i]) for i in range(3)]

    def add_view(self, view):
        """Adds a view to this model."""
        self._views.append(view)

    def update(self):
        """Sends an update request to all the views."""
        for view in self._views:
            view.update()

    def is_key_down(self, letter):
        return self._key_state.get(letter, False)

    def is_lamp_on(self, letter):
        return self._lamp_state.get(letter, False)

    def key_pressed(self, letter):
        self._key_state[letter] = True
        self._advance_rotors()

        index = ord(letter) - ord('A')

        # Pass through the rotors from right to left
        for rotor in reversed(self._rotors):
            index = self._apply_permutation(index, rotor.get_permutation(), rotor.get_offset())

        # Pass through the reflector
        index = self._apply_permutation(index, REFLECTOR_PERMUTATION, 0)

        # Pass through the rotors from left to right (inverse)
        for rotor in self._rotors:
            index = self._apply_permutation(index, rotor.get_inverse_permutation(), rotor.get_offset())

        encrypted_letter = ALPHABET[index]
        self._lamp_state[encrypted_letter] = True
        self.update()

    def _advance_rotors(self):
        carry = self._rotors[2].advance()
        if carry:
            carry = self._rotors[1].advance()
            if carry:
                self._rotors[0].advance()

    def key_released(self, letter):
        self._key_state[letter] = False
        for l in ALPHABET:
            self._lamp_state[l] = False
        self.update()

    def get_rotor_letter(self, index):
        offset = self._rotors[index].get_offset()
        return chr((ord('A') + offset) % 26 + ord('A'))

    def rotor_clicked(self, index):
        self._rotors[index].advance()
        self.update()

    def _apply_permutation(self, index, permutation, offset):
        index = (index + offset) % 26
        encrypted_letter = permutation[index]
        return (ord(encrypted_letter) - ord('A') - offset) % 26

def enigma():
    """Runs the Enigma simulator."""
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

if __name__ == "__main__":
    enigma()