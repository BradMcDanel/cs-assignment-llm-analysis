from EnigmaView import EnigmaView
from EnigmaConstants import ROTOR_PERMUTATIONS, REFLECTOR_PERMUTATION

class EnigmaRotor:
    def __init__(self, permutation):
        self.permutation = permutation
        self.offset = 0
        self.inverse_permutation = self.invert_permutation(permutation)

    def invert_permutation(self, permutation):
        inverse = [''] * 26
        for i, char in enumerate(permutation):
            inverse[ord(char) - ord('A')] = chr(i + ord('A'))
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

    def apply_permutation(self, index, offset=None):
        if offset is None:
            offset = self.offset
        shifted_index = (index + offset) % 26
        translated_char = self.permutation[shifted_index]
        translated_index = (ord(translated_char) - ord('A') - offset) % 26
        return translated_index

    def apply_inverse_permutation(self, index, offset=None):
        if offset is None:
            offset = self.offset
        shifted_index = (index + offset) % 26
        translated_char = self.inverse_permutation[shifted_index]
        translated_index = (ord(translated_char) - ord('A') - offset) % 26
        return translated_index

class EnigmaModel:
    def __init__(self):
        self._views = []
        self.keys_state = {chr(i + ord('A')): False for i in range(26)}
        self.lamps_state = {chr(i + ord('A')): False for i in range(26)}
        self.rotors = [EnigmaRotor(permutation) for permutation in ROTOR_PERMUTATIONS]

    def add_view(self, view):
        self._views.append(view)

    def update(self):
        for view in self._views:
            view.update()

    def key_pressed(self, letter):
        index = ord(letter) - ord('A')
        self.keys_state[letter] = True
        self.encrypt_letter(index)
        self.update()

    def key_released(self, letter):
        self.keys_state[letter] = False
        self.lamps_state = {key: False for key in self.lamps_state}
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
        return chr(offset + ord('A'))

    def encrypt_letter(self, index):
        # Advance the fast rotor before encryption
        carry = self.rotors[2].advance()
        if carry:
            carry = self.rotors[1].advance()
            if carry:
                self.rotors[0].advance()

        # Encrypt through rotors right to left
        for rotor in reversed(self.rotors):
            index = rotor.apply_permutation(index)

        # Reflector
        reflected_char = REFLECTOR_PERMUTATION[index]
        index = ord(reflected_char) - ord('A')

        # Encrypt through rotors left to right
        for rotor in self.rotors:
            index = rotor.apply_inverse_permutation(index)

        # Set the corresponding lamp on
        encrypted_letter = chr(index + ord('A'))
        self.lamps_state[encrypted_letter] = True

def enigma():
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

if __name__ == "__main__":
    enigma()