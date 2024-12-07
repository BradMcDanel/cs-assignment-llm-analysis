# File: EnigmaModel.py

from EnigmaView import EnigmaView
from EnigmaConstants import ALPHABET, ROTOR_PERMUTATIONS, REFLECTOR_PERMUTATION
from EnigmaRotor import EnigmaRotor

class EnigmaModel:
    def __init__(self):
        self._views = []
        self._rotors = [EnigmaRotor(ROTOR_PERMUTATIONS[i]) for i in range(3)]
        self._key_state = {letter: False for letter in ALPHABET}
        self._lamp_state = {letter: False for letter in ALPHABET}

    def add_view(self, view):
        self._views.append(view)

    def update(self):
        for view in self._views:
            view.update()

    def is_key_down(self, letter):
        return self._key_state[letter]

    def is_lamp_on(self, letter):
        return self._lamp_state[letter]

    def key_pressed(self, letter):
        self._key_state[letter] = True
        self.advance_rotors()
        encrypted_index = self.encrypt(letter)
        self._lamp_state[ALPHABET[encrypted_index]] = True
        self.update()

    def key_released(self, letter):
        self._key_state[letter] = False
        for l in ALPHABET:
            self._lamp_state[l] = False
        self.update()

    def get_rotor_letter(self, index):
        offset = self._rotors[index].get_offset()
        return ALPHABET[offset]

    def rotor_clicked(self, index):
        self._rotors[index].advance()
        self.update()

    def advance_rotors(self):
        if self._rotors[2].advance():
            if self._rotors[1].advance():
                self._rotors[0].advance()

    def encrypt(self, letter):
        index = ALPHABET.index(letter)
        for rotor in reversed(self._rotors):
            index = rotor.apply_permutation(index, rotor.get_offset())
        
        index = (ord(REFLECTOR_PERMUTATION[index]) - ord('A')) % 26
        
        for rotor in self._rotors:
            index = rotor.apply_inverse_permutation(index, rotor.get_offset())
        
        return index

def enigma():
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

if __name__ == "__main__":
    enigma()