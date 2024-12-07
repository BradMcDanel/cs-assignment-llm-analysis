from EnigmaView import EnigmaView
from EnigmaConstants import ROTOR_PERMUTATIONS, REFLECTOR_PERMUTATION

class EnigmaRotor:
    def __init__(self, permutation):
        self.permutation = permutation
        self.inverse_permutation = self.invert_permutation(permutation)
        self.offset = 0

    def invert_permutation(self, permutation):
        inverse = [''] * 26
        for i, char in enumerate(permutation):
            inverse[ord(char) - ord('A')] = chr(i + ord('A'))
        return ''.join(inverse)

    def get_offset(self):
        return self.offset

    def get_permutation(self):
        return self.permutation

    def advance(self):
        self.offset = (self.offset + 1) % 26
        return self.offset == 0

    def apply_permutation(self, index, offset, use_inverse=False):
        perm = self.inverse_permutation if use_inverse else self.permutation
        index = (index + offset) % 26
        char = perm[index]
        return (ord(char) - ord('A') - offset) % 26

class EnigmaModel:
    def __init__(self):
        self._views = []
        self._keys_state = {chr(i): False for i in range(ord('A'), ord('Z') + 1)}
        self._lamps_state = {chr(i): False for i in range(ord('A'), ord('Z') + 1)}
        self.rotors = [EnigmaRotor(ROTOR_PERMUTATIONS[i]) for i in range(3)]

    def add_view(self, view):
        self._views.append(view)

    def update(self):
        for view in self._views:
            view.update()

    def key_pressed(self, letter):
        self._keys_state[letter] = True
        self.perform_encryption(letter)
        self.update()

    def key_released(self, letter):
        self._keys_state[letter] = False
        self.update()

    def is_key_down(self, letter):
        return self._keys_state.get(letter, False)

    def is_lamp_on(self, letter):
        return self._lamps_state.get(letter, False)

    def rotor_clicked(self, index):
        self.rotors[index].advance()
        self.update()

    def get_rotor_letter(self, index):
        offset = self.rotors[index].get_offset()
        return chr((ord('A') + offset) % 26)

    def perform_encryption(self, letter):
        index = ord(letter) - ord('A')
        self.rotors[0].advance()  # The fast rotor always advances on key press

        # Forward pass through the rotors
        for rotor in self.rotors:
            index = rotor.apply_permutation(index, rotor.get_offset())

        # Reflector
        index = (ord(REFLECTOR_PERMUTATION[index]) - ord('A')) % 26

        # Backward pass through the rotors
        for rotor in reversed(self.rotors):
            index = rotor.apply_permutation(index, rotor.get_offset(), use_inverse=True)

        encrypted_letter = chr(index + ord('A'))
        for lamp in self._lamps_state:
            self._lamps_state[lamp] = False
        self._lamps_state[encrypted_letter] = True

def enigma():
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

if __name__ == "__main__":
    enigma()