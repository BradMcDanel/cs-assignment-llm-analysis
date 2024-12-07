from EnigmaView import EnigmaView
from EnigmaConstants import ALPHABET, N_ROTORS, ROTOR_PERMUTATIONS

class EnigmaModel:
    def __init__(self):
        self._rotors = [EnigmaRotor(perm) for perm in ROTOR_PERMUTATIONS]
        self._views = []

    def add_view(self, view):
        self._views.append(view)

    def update(self):
        for view in self._views:
            view.update()

    def is_key_down(self, letter):
        return False

    def is_lamp_on(self, letter):
        return False

    def key_pressed(self, letter):
        # Implement key press functionality here
        self.update()

    def key_released(self, letter):
        # Implement key release functionality here
        self.update()

    def get_rotor_letter(self, index):
        return self._rotors[index].get_letter()

    def rotor_clicked(self, index):
        self._rotors[index].advance()
        self.update()

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