from EnigmaView import EnigmaView
from EnigmaConstants import ROTOR_PERMUTATIONS, REFLECTOR_PERMUTATION

class EnigmaRotor:
    def __init__(self, permutation):
        self.permutation = permutation
        self.inverse_permutation = self.invert_key(permutation)
        self.offset = 0

    def invert_key(self, key):
        inverse = [''] * 26
        for i, char in enumerate(key):
            index = ord(char) - ord('A')
            inverse[index] = chr(i + ord('A'))
        return ''.join(inverse)

    def get_offset(self):
        return self.offset

    def get_permutation(self):
        return self.permutation

    def get_inverse_permutation(self):
        return self.inverse_permutation

    def advance(self):
        self.offset = (self.offset + 1) % 26
        return self.offset == 0

class EnigmaModel:
    def __init__(self):
        self._views = []
        self.keys_state = {chr(i): False for i in range(ord('A'), ord('Z') + 1)}
        self.lamps_state = {chr(i): False for i in range(ord('A'), ord('Z') + 1)}
        self.rotors = [EnigmaRotor(permutation) for permutation in ROTOR_PERMUTATIONS]

    def add_view(self, view):
        self._views.append(view)

    def update(self):
        for view in self._views:
            view.update()

    def key_pressed(self, letter):
        self.keys_state[letter] = True
        self.activate_lamp(letter)
        self.advance_rotors()
        self.update()

    def key_released(self, letter):
        self.keys_state[letter] = False
        self.update()

    def is_key_down(self, letter):
        return self.keys_state.get(letter, False)

    def is_lamp_on(self, letter):
        return self.lamps_state.get(letter, False)

    def rotor_clicked(self, index):
        self.rotors[index].advance()
        self.update()

    def get_rotor_letter(self, index):
        offset = self.rotors[index].get_offset()
        return chr((ord('A') + offset) % 26)

    def activate_lamp(self, letter):
        index = ord(letter) - ord('A')
        permuted_index = self.encrypt(index)
        lamp_letter = chr(permuted_index + ord('A'))
        self.lamps_state = {key: False for key in self.lamps_state}
        self.lamps_state[lamp_letter] = True

    def encrypt(self, index):
        for rotor in self.rotors:
            perm = rotor.get_permutation()
            index = (ord(perm[(index + rotor.get_offset()) % 26]) - ord('A') - rotor.get_offset()) % 26
        index = (ord(REFLECTOR_PERMUTATION[index]) - ord('A')) % 26
        for rotor in reversed(self.rotors):
            inv_perm = rotor.get_inverse_permutation()
            index = (ord(inv_perm[(index + rotor.get_offset()) % 26]) - ord('A') - rotor.get_offset()) % 26
        return index

    def advance_rotors(self):
        carry = self.rotors[0].advance()
        if carry:
            carry = self.rotors[1].advance()
            if carry:
                self.rotors[2].advance()

def enigma():
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

if __name__ == "__main__":
    enigma()