from EnigmaView import EnigmaView
from EnigmaConstants import ALPHABET, ROTOR_PERMUTATIONS, REFLECTOR_PERMUTATION, N_ROTORS

class EnigmaRotor:
    def __init__(self, permutation):
        self._permutation = permutation
        self._offset = 0
        self._inverse_permutation = self.invert_key(permutation)

    def get_offset(self):
        return self._offset

    def get_permutation(self):
        return self._permutation

    def get_inverse_permutation(self):
        return self._inverse_permutation

    def advance(self):
        self._offset = (self._offset + 1) % 26
        return self._offset == 0

    def invert_key(self, key):
        inverse_key = [''] * 26
        for i, letter in enumerate(key):
            inverse_key[ord(letter) - ord('A')] = chr(i + ord('A'))
        return ''.join(inverse_key)

    def apply_permutation(self, index, reverse=False):
        if reverse:
            permutation = self._inverse_permutation
        else:
            permutation = self._permutation
        shifted_index = (index + self._offset) % 26
        letter = permutation[shifted_index]
        return (ord(letter) - ord('A') - self._offset) % 26

class EnigmaModel:
    def __init__(self):
        self._views = []
        self._keys = {letter: False for letter in ALPHABET}
        self._lamps = {letter: False for letter in ALPHABET}
        self._rotors = [EnigmaRotor(ROTOR_PERMUTATIONS[i]) for i in range(N_ROTORS)]

    def add_view(self, view):
        self._views.append(view)

    def update(self):
        for view in self._views:
            view.update()

    def is_key_down(self, letter):
        return self._keys[letter]

    def is_lamp_on(self, letter):
        return self._lamps[letter]

    def key_pressed(self, letter):
        self._keys[letter] = True
        self.process_key(letter)
        self.update()

    def key_released(self, letter):
        self._keys[letter] = False
        self.update()

    def get_rotor_letter(self, index):
        offset = self._rotors[index].get_offset()
        return ALPHABET[offset]

    def rotor_clicked(self, index):
        self._rotors[index].advance()
        self.update()

    def process_key(self, letter):
        self.advance_rotors()
        index = ALPHABET.index(letter)
        for rotor in reversed(self._rotors):
            index = rotor.apply_permutation(index)
        index = ALPHABET.index(REFLECTOR_PERMUTATION[index])
        for rotor in self._rotors:
            index = rotor.apply_permutation(index, reverse=True)
        encrypted_letter = ALPHABET[index]
        self._lamps[encrypted_letter] = True

    def advance_rotors(self):
        carry = self._rotors[2].advance()
        if carry:
            carry = self._rotors[1].advance()
            if carry:
                self._rotors[0].advance()

def enigma():
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

if __name__ == "__main__":
    enigma()