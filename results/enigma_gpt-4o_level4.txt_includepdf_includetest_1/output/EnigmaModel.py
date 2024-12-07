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
            inverse[ALPHABET.index(char)] = ALPHABET[i]
        return ''.join(inverse)

    def get_offset(self):
        return self.offset

    def get_permutation(self):
        return self.permutation

    def advance(self):
        self.offset = (self.offset + 1) % 26
        return self.offset == 0

    def apply_permutation(self, index, direction='right'):
        shifted_index = (index + self.offset) % 26
        if direction == 'right':
            char = self.permutation[shifted_index]
        else:
            char = self.inverse_permutation[shifted_index]
        result_index = (ALPHABET.index(char) - self.offset) % 26
        return result_index

class EnigmaModel:
    def __init__(self):
        self._views = []
        self.keys_pressed = {}
        self.lamps_on = {}
        self.rotors = [EnigmaRotor(ROTOR_PERMUTATIONS[i]) for i in range(3)]

    def add_view(self, view):
        self._views.append(view)

    def update(self):
        for view in self._views:
            view.update()

    def is_key_down(self, letter):
        return self.keys_pressed.get(letter, False)

    def is_lamp_on(self, letter):
        return self.lamps_on.get(letter, False)

    def key_pressed(self, letter):
        self.keys_pressed[letter] = True
        self.encrypt(letter)
        self.update()

    def key_released(self, letter):
        self.keys_pressed[letter] = False
        self.update()

    def encrypt(self, letter):
        index = ALPHABET.index(letter)
        self.advance_rotors()
        for rotor in reversed(self.rotors):
            index = rotor.apply_permutation(index, 'right')

        reflector_index = ALPHABET.index(REFLECTOR_PERMUTATION[index])
        index = reflector_index

        for rotor in self.rotors:
            index = rotor.apply_permutation(index, 'left')

        encrypted_letter = ALPHABET[index]
        self.lamps_on = {encrypted_letter: True}

    def advance_rotors(self):
        if self.rotors[2].advance():
            if self.rotors[1].advance():
                self.rotors[0].advance()

    def get_rotor_letter(self, index):
        return ALPHABET[self.rotors[index].get_offset()]

    def rotor_clicked(self, index):
        self.rotors[index].advance()
        self.update()

def enigma():
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

if __name__ == "__main__":
    enigma()