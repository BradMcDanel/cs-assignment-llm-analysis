class EnigmaRotor:
    def __init__(self, permutation):
        self.permutation = permutation
        self.offset = 0
        self.inverse_permutation = self.invert_key(permutation)

    def get_offset(self):
        return self.offset

    def get_permutation(self):
        return self.permutation

    def advance(self):
        self.offset = (self.offset + 1) % 26
        return self.offset == 0

    def invert_key(self, key):
        inverse_key = [''] * 26
        for i, c in enumerate(key):
            inverse_key[ord(c) - ord('A')] = chr(ord('A') + i)
        return ''.join(inverse_key)

def apply_permutation(index, permutation, offset):
    shifted_index = (index + offset) % 26
    new_char = permutation[shifted_index]
    new_index = (ord(new_char) - ord('A') - offset) % 26
    return new_index

### EnigmaModel.py ###

from EnigmaView import EnigmaView
from EnigmaRotor import EnigmaRotor, apply_permutation
from EnigmaConstants import ROTOR_PERMUTATIONS, REFLECTOR_PERMUTATION

class EnigmaModel:

    def __init__(self):
        """Creates a new EnigmaModel with no views."""
        self._views = []
        self._key_state = {}
        self._lamp_state = {}
        self._rotors = [EnigmaRotor(ROTOR_PERMUTATIONS[i]) for i in range(3)]

    def add_view(self, view):
        """Adds a view to this model."""
        self._views.append(view)

    def update(self):
        """Sends an update request to all the views."""
        for view in self._views:
            view.update()

    def key_pressed(self, letter):
        self._key_state[letter] = True
        index = ord(letter) - ord('A')
        rotor = self._rotors[0]
        encrypted_index = apply_permutation(index, rotor.get_permutation(), rotor.get_offset())
        encrypted_letter = chr(encrypted_index + ord('A'))
        self._lamp_state[encrypted_letter] = True
        self.update()

    def key_released(self, letter):
        self._key_state[letter] = False
        self._lamp_state = {}  # Reset all lamp states
        self.update()

    def is_key_down(self, letter):
        return self._key_state.get(letter, False)

    def is_lamp_on(self, letter):
        return self._lamp_state.get(letter, False)

    def rotor_clicked(self, index):
        self._rotors[index].advance()
        self.update()

    def get_rotor_letter(self, index):
        offset = self._rotors[index].get_offset()
        return chr((ord('A') + offset) % 26)

def enigma():
    """Runs the Enigma simulator."""
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

# Startup code

if __name__ == "__main__":
    enigma()