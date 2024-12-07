from EnigmaView import EnigmaView
from EnigmaConstants import ROTOR_PERMUTATIONS, REFLECTOR_PERMUTATION

class EnigmaRotor:
    def __init__(self, permutation):
        self._permutation = permutation
        self._inverse_permutation = self.invert_permutation(permutation)
        self._offset = 0

    def invert_permutation(self, permutation):
        inverse = [''] * 26
        for index, char in enumerate(permutation):
            inverse[ord(char) - ord('A')] = chr(index + ord('A'))
        return ''.join(inverse)

    def get_offset(self):
        return self._offset

    def get_permutation(self):
        return self._permutation

    def advance(self):
        self._offset = (self._offset + 1) % 26
        return self._offset == 0  # Returns True if a full rotation occurs

    def apply_permutation(self, index, reverse=False):
        permutation = self._inverse_permutation if reverse else self._permutation
        shifted_index = (index + self._offset) % 26
        translated_char = permutation[shifted_index]
        return (ord(translated_char) - ord('A') - self._offset) % 26

class EnigmaModel:
    def __init__(self):
        self._views = []
        self._key_states = {chr(i): False for i in range(ord('A'), ord('Z') + 1)}
        self._lamp_states = {chr(i): False for i in range(ord('A'), ord('Z') + 1)}
        self._rotors = [EnigmaRotor(ROTOR_PERMUTATIONS[i]) for i in range(3)]

    def add_view(self, view):
        self._views.append(view)

    def update(self):
        for view in self._views:
            view.update()

    def key_pressed(self, letter):
        self._key_states[letter] = True
        self.process_encryption(letter)
        self.update()

    def key_released(self, letter):
        self._key_states[letter] = False
        self.update()

    def is_key_down(self, letter):
        return self._key_states[letter]

    def is_lamp_on(self, letter):
        return self._lamp_states[letter]

    def rotor_clicked(self, index):
        self._rotors[index].advance()
        self.update()

    def get_rotor_letter(self, index):
        offset = self._rotors[index].get_offset()
        return chr(ord('A') + offset)

    def process_encryption(self, letter):
        index = ord(letter) - ord('A')
        for rotor in reversed(self._rotors):
            index = rotor.apply_permutation(index)
        index = (ord(REFLECTOR_PERMUTATION[index]) - ord('A'))
        for rotor in self._rotors:
            index = rotor.apply_permutation(index, reverse=True)
        encrypted_letter = chr(index + ord('A'))
        self._lamp_states[encrypted_letter] = True
        self._lamp_states = {k: False for k in self._lamp_states}  # Reset lamps
        self.advance_rotors()

    def advance_rotors(self):
        carry = True
        for rotor in self._rotors:
            if carry:
                carry = rotor.advance()
            else:
                break

def enigma():
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

if __name__ == "__main__":
    enigma()