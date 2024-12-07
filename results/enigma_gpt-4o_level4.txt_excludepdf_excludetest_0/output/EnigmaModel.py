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
            index = ord(char) - ord('A')
            inverse[index] = chr(i + ord('A'))
        return ''.join(inverse)
    
    def get_offset(self):
        return self.offset

    def get_permutation(self, reverse=False):
        return self.inverse_permutation if reverse else self.permutation

    def advance(self):
        self.offset = (self.offset + 1) % 26
        return self.offset == 0

    def apply_permutation(self, index, reverse=False):
        offset_index = (index + self.offset) % 26
        perm = self.get_permutation(reverse)
        translated_char = perm[offset_index]
        translated_index = (ord(translated_char) - ord('A') - self.offset) % 26
        return translated_index

class EnigmaModel:
    def __init__(self):
        self._views = []
        self.keys_state = {chr(i): False for i in range(ord('A'), ord('Z') + 1)}
        self.lamps_state = {chr(i): False for i in range(ord('A'), ord('Z') + 1)}
        self.rotors = [EnigmaRotor(ROTOR_PERMUTATIONS[i]) for i in range(3)]

    def add_view(self, view):
        self._views.append(view)

    def update(self):
        for view in self._views:
            view.update()

    def key_pressed(self, letter):
        self.keys_state[letter] = True
        self.advance_rotors()
        encrypted_index = self.encrypt(ord(letter) - ord('A'))
        encrypted_letter = chr(encrypted_index + ord('A'))
        self.lamps_state[encrypted_letter] = True
        self.update()

    def key_released(self, letter):
        self.keys_state[letter] = False
        for lamp in self.lamps_state:
            self.lamps_state[lamp] = False
        self.update()

    def is_key_down(self, letter):
        return self.keys_state.get(letter, False)

    def is_lamp_on(self, letter):
        return self.lamps_state.get(letter, False)

    def rotor_clicked(self, index):
        self.rotors[index].advance()
        self.update()

    def get_rotor_letter(self, index):
        return chr((self.rotors[index].get_offset() + ord('A')))

    def advance_rotors(self):
        if self.rotors[0].advance():
            if self.rotors[1].advance():
                self.rotors[2].advance()

    def encrypt(self, index):
        # Pass through the rotors from right to left
        for rotor in self.rotors:
            index = rotor.apply_permutation(index)
        # Pass through the reflector
        index = (ord(REFLECTOR_PERMUTATION[index]) - ord('A')) % 26
        # Pass back through the rotors from left to right
        for rotor in reversed(self.rotors):
            index = rotor.apply_permutation(index, reverse=True)
        return index

def enigma():
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

if __name__ == "__main__":
    enigma()