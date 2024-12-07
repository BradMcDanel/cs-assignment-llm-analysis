from EnigmaView import EnigmaView
from EnigmaConstants import ALPHABET, ROTOR_PERMUTATIONS, REFLECTOR_PERMUTATION

class EnigmaRotor:
    def __init__(self, permutation):
        self.permutation = permutation
        self.offset = 0
        self.inverse_permutation = self.invert_permutation(permutation)

    def invert_permutation(self, permutation):
        inverse = [''] * 26
        for i, char in enumerate(permutation):
            index = ALPHABET.index(char)
            inverse[index] = ALPHABET[i]
        return ''.join(inverse)

    def advance(self):
        self.offset = (self.offset + 1) % 26
        return self.offset == 0

    def get_offset(self):
        return self.offset

    def get_permutation(self):
        return self.permutation

    def apply_permutation(self, index, reverse=False):
        effective_permutation = self.inverse_permutation if reverse else self.permutation
        index = (index + self.offset) % 26
        char = effective_permutation[index]
        new_index = (ALPHABET.index(char) - self.offset) % 26
        return new_index

class EnigmaModel:
    def __init__(self):
        self._views = []
        self.keys_state = {letter: False for letter in ALPHABET}
        self.lamps_state = {letter: False for letter in ALPHABET}
        self.rotors = [EnigmaRotor(perm) for perm in ROTOR_PERMUTATIONS]

    def add_view(self, view):
        self._views.append(view)

    def update(self):
        for view in self._views:
            view.update()

    def key_pressed(self, letter):
        self.keys_state[letter] = True
        index = ALPHABET.index(letter)
        self.advance_rotors()
        index = self.encrypt(index)
        lamp_letter = ALPHABET[index]
        self.lamps_state[lamp_letter] = True
        self.update()

    def key_released(self, letter):
        self.keys_state[letter] = False
        for key in self.lamps_state:
            self.lamps_state[key] = False
        self.update()

    def is_key_down(self, letter):
        return self.keys_state[letter]

    def is_lamp_on(self, letter):
        return self.lamps_state[letter]

    def rotor_clicked(self, index):
        self.rotors[index].advance()
        self.update()

    def get_rotor_letter(self, index):
        offset = self.rotors[index].get_offset()
        return ALPHABET[offset]

    def advance_rotors(self):
        carry = self.rotors[-1].advance()
        if carry:
            carry = self.rotors[-2].advance()
            if carry:
                self.rotors[-3].advance()

    def encrypt(self, index):
        for rotor in reversed(self.rotors):
            index = rotor.apply_permutation(index)
        index = ALPHABET.index(REFLECTOR_PERMUTATION[index])
        for rotor in self.rotors:
            index = rotor.apply_permutation(index, reverse=True)
        return index

def enigma():
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

if __name__ == "__main__":
    enigma()