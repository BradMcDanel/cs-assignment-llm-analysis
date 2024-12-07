from EnigmaView import EnigmaView
from EnigmaConstants import ROTOR_PERMUTATIONS, REFLECTOR_PERMUTATION

class EnigmaRotor:
    def __init__(self, permutation):
        self._permutation = permutation
        self._inverse_permutation = self._invert_key(permutation)
        self._offset = 0

    def _invert_key(self, key):
        return ''.join(chr(key.index(chr(i + 65)) + 65) for i in range(26))

    def get_offset(self):
        return self._offset

    def get_permutation(self):
        return self._permutation

    def advance(self):
        self._offset = (self._offset + 1) % 26
        return self._offset == 0

    def apply_permutation(self, index, forward=True):
        permutation = self._permutation if forward else self._inverse_permutation
        shifted_index = (index + self._offset) % 26
        new_index = ord(permutation[shifted_index]) - 65
        return (new_index - self._offset) % 26

def apply_permutation(index, permutation, offset):
    shifted_index = (index + offset) % 26
    new_index = ord(permutation[shifted_index]) - 65
    return (new_index - offset) % 26

class EnigmaModel:
    def __init__(self):
        self._views = []
        self._keys_pressed = {chr(i + 65): False for i in range(26)}
        self._lamps_on = {chr(i + 65): False for i in range(26)}
        self._rotors = [EnigmaRotor(perm) for perm in ROTOR_PERMUTATIONS]

    def add_view(self, view):
        self._views.append(view)

    def update(self):
        for view in self._views:
            view.update()

    def key_pressed(self, letter):
        self._keys_pressed[letter] = True
        self._advance_rotors()
        encrypted_letter = self._encrypt(letter)
        self._lamps_on[encrypted_letter] = True
        self.update()

    def key_released(self, letter):
        self._keys_pressed[letter] = False
        for lamp in self._lamps_on:
            self._lamps_on[lamp] = False
        self.update()

    def is_key_down(self, letter):
        return self._keys_pressed[letter]

    def is_lamp_on(self, letter):
        return self._lamps_on[letter]

    def rotor_clicked(self, index):
        self._rotors[index].advance()
        self.update()

    def get_rotor_letter(self, index):
        offset = self._rotors[index].get_offset()
        return chr((offset + 65) % 91)

    def _advance_rotors(self):
        if self._rotors[2].advance():
            if self._rotors[1].advance():
                self._rotors[0].advance()

    def _encrypt(self, letter):
        index = ord(letter) - 65
        
        # Right to left through rotors
        for rotor in reversed(self._rotors):
            index = rotor.apply_permutation(index)

        # Through reflector
        index = apply_permutation(index, REFLECTOR_PERMUTATION, 0)

        # Left to right through rotors
        for rotor in self._rotors:
            index = rotor.apply_permutation(index, forward=False)

        return chr(index + 65)

def enigma():
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

if __name__ == "__main__":
    enigma()