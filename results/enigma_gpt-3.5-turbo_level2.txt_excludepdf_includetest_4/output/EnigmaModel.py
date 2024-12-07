# Enigma Model implementation

from EnigmaView import EnigmaView
from EnigmaConstants import ROTOR_PERMUTATIONS

class EnigmaModel:
    def __init__(self):
        self._views = []
        self._keys_state = {letter: False for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
        self._lamps_state = {letter: False for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
        self._rotors = [EnigmaRotor(perm) for perm in ROTOR_PERMUTATIONS]

    def add_view(self, view):
        self._views.append(view)

    def update(self):
        for view in self._views:
            view.update()

    def key_pressed(self, letter):
        self._keys_state[letter] = True
        self.update()

    def key_released(self, letter):
        self._keys_state[letter] = False
        self.update()

    def is_key_down(self, letter):
        return self._keys_state[letter]

    def is_lamp_on(self, letter):
        return self._lamps_state[letter]

    def rotor_clicked(self, index):
        self._rotors[index].advance()
        self.update()

    def get_rotor_letter(self, index):
        rotor = self._rotors[index]
        offset = rotor.get_offset()
        permutation = rotor.get_permutation()
        letter_index = (offset) % 26
        return permutation[letter_index]

class EnigmaRotor:
    def __init__(self, permutation):
        self._permutation = permutation
        self._offset = 0

    def get_offset(self):
        return self._offset

    def get_permutation(self):
        return self._permutation

    def advance(self):
        self._offset = (self._offset + 1) % 26