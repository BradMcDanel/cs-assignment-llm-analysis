from EnigmaView import EnigmaView
from EnigmaConstants import ROTOR_PERMUTATIONS, REFLECTOR_PERMUTATION
from EnigmaRotor import EnigmaRotor, apply_permutation, invert_key

class EnigmaModel:
    def __init__(self):
        self._views = []
        self._keys_pressed = {chr(65 + i): False for i in range(26)}
        self._lamps_on = {chr(65 + i): False for i in range(26)}
        self._rotors = [
            EnigmaRotor(ROTOR_PERMUTATIONS[0]),
            EnigmaRotor(ROTOR_PERMUTATIONS[1]),
            EnigmaRotor(ROTOR_PERMUTATIONS[2])
        ]

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
        return chr((self._rotors[index].get_offset() + 65) % 26)

    def _advance_rotors(self):
        if self._rotors[2].advance():
            if self._rotors[1].advance():
                self._rotors[0].advance()

    def _encrypt(self, letter):
        index = ord(letter) - 65
        for rotor in reversed(self._rotors):
            index = apply_permutation(index, rotor.get_permutation(), rotor.get_offset())
        index = apply_permutation(index, REFLECTOR_PERMUTATION, 0)
        for rotor in self._rotors:
            index = apply_permutation(index, rotor.get_inverse_permutation(), rotor.get_offset())
        return chr(index + 65)

def enigma():
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

if __name__ == "__main__":
    enigma()