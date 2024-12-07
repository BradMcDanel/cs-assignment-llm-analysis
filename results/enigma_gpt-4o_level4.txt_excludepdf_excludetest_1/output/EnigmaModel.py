from EnigmaView import EnigmaView
from EnigmaConstants import ROTOR_PERMUTATIONS, REFLECTOR_PERMUTATION

class EnigmaRotor:
    def __init__(self, permutation):
        self.permutation = permutation
        self.offset = 0
        self.inverse_permutation = self.invert_key(permutation)

    def get_offset(self):
        return self.offset

    def get_permutation(self):
        return self.permutation

    def get_inverse_permutation(self):
        return self.inverse_permutation

    def advance(self):
        self.offset = (self.offset + 1) % 26
        return self.offset == 0

    @staticmethod
    def invert_key(permutation):
        inverse = [''] * 26
        for i, char in enumerate(permutation):
            inverse[ord(char) - ord('A')] = chr(i + ord('A'))
        return ''.join(inverse)

class EnigmaModel:
    def __init__(self):
        self._views = []
        self.keys_state = {chr(i + ord('A')): False for i in range(26)}
        self.lamps_state = {chr(i + ord('A')): False for i in range(26)}
        self.rotors = [EnigmaRotor(p) for p in ROTOR_PERMUTATIONS]

    def add_view(self, view):
        self._views.append(view)

    def update(self):
        for view in self._views:
            view.update()

    def key_pressed(self, letter):
        self.keys_state[letter] = True
        self.lamps_state = {k: False for k in self.lamps_state}  # Reset lamps

        # Advance rotors
        if self.rotors[2].advance():
            if self.rotors[1].advance():
                self.rotors[0].advance()

        # Encrypt the letter
        index = ord(letter) - ord('A')
        for rotor in reversed(self.rotors):
            index = self.apply_permutation(index, rotor.get_permutation(), rotor.get_offset())
        index = self.apply_permutation(index, REFLECTOR_PERMUTATION, 0)
        for rotor in self.rotors:
            index = self.apply_permutation(index, rotor.get_inverse_permutation(), rotor.get_offset())

        encrypted_letter = chr(index + ord('A'))
        self.lamps_state[encrypted_letter] = True

        self.update()

    def key_released(self, letter):
        self.keys_state[letter] = False
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
        return chr((ord('A') + offset) % 26)

    @staticmethod
    def apply_permutation(index, permutation, offset):
        shifted_index = (index + offset) % 26
        letter = permutation[shifted_index]
        return (ord(letter) - ord('A') - offset) % 26

def enigma():
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

if __name__ == "__main__":
    enigma()