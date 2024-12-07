from EnigmaView import EnigmaView
from EnigmaConstants import ALPHABET, ROTOR_PERMUTATIONS, REFLECTOR_PERMUTATION

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
        self.offset = (self.offset + 1) % len(ALPHABET)
        return self.offset == 0

    def invert_key(self, key):
        inverse = [''] * len(key)
        for i, char in enumerate(key):
            inverse[ALPHABET.index(char)] = ALPHABET[i]
        return ''.join(inverse)

class EnigmaModel:
    def __init__(self):
        self._views = []
        self.keys = {letter: False for letter in ALPHABET}
        self.lamps = {letter: False for letter in ALPHABET}
        self.rotors = [EnigmaRotor(ROTOR_PERMUTATIONS[i]) for i in range(3)]

    def add_view(self, view):
        self._views.append(view)

    def update(self):
        for view in self._views:
            view.update()

    def key_pressed(self, letter):
        self.keys[letter] = True
        self.lamps = {l: False for l in ALPHABET}
        index = ALPHABET.index(letter)
        self.advance_rotors()
        encrypted_index = self.encrypt(index)
        self.lamps[ALPHABET[encrypted_index]] = True
        self.update()

    def key_released(self, letter):
        self.keys[letter] = False
        self.update()

    def is_key_down(self, letter):
        return self.keys[letter]

    def is_lamp_on(self, letter):
        return self.lamps[letter]

    def rotor_clicked(self, index):
        self.rotors[index].advance()
        self.update()

    def get_rotor_letter(self, index):
        return ALPHABET[self.rotors[index].get_offset()]

    def advance_rotors(self):
        if self.rotors[2].advance():
            if self.rotors[1].advance():
                self.rotors[0].advance()

    def encrypt(self, index):
        index = self.apply_permutation(index, self.rotors[2].get_permutation(), self.rotors[2].get_offset())
        index = self.apply_permutation(index, self.rotors[1].get_permutation(), self.rotors[1].get_offset())
        index = self.apply_permutation(index, self.rotors[0].get_permutation(), self.rotors[0].get_offset())
        index = self.apply_permutation(index, REFLECTOR_PERMUTATION, 0)
        index = self.apply_permutation(index, self.rotors[0].inverse_permutation, self.rotors[0].get_offset())
        index = self.apply_permutation(index, self.rotors[1].inverse_permutation, self.rotors[1].get_offset())
        index = self.apply_permutation(index, self.rotors[2].inverse_permutation, self.rotors[2].get_offset())
        return index

    def apply_permutation(self, index, permutation, offset):
        shifted_index = (index + offset) % len(ALPHABET)
        letter = permutation[shifted_index]
        new_index = ALPHABET.index(letter)
        return (new_index - offset) % len(ALPHABET)

def enigma():
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

if __name__ == "__main__":
    enigma()