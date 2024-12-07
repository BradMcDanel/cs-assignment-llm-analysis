from EnigmaView import EnigmaView
from EnigmaConstants import ROTOR_PERMUTATIONS, REFLECTOR_PERMUTATION

class EnigmaRotor:
    def __init__(self, permutation):
        self.permutation = permutation
        self.inverted_permutation = self.invert_key(permutation)
        self.offset = 0

    def invert_key(self, key):
        inverted = [''] * 26
        for i, char in enumerate(key):
            inverted[ord(char) - ord('A')] = chr(i + ord('A'))
        return ''.join(inverted)

    def get_offset(self):
        return self.offset

    def get_permutation(self):
        return self.permutation

    def advance(self):
        self.offset = (self.offset + 1) % 26
        return self.offset == 0

    def apply_permutation(self, index, offset, reverse=False):
        if reverse:
            perm = self.inverted_permutation
        else:
            perm = self.permutation

        shifted_index = (index + offset) % 26
        new_char = perm[shifted_index]
        new_index = (ord(new_char) - ord('A') - offset) % 26
        return new_index

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

        input_index = ord(letter) - ord('A')
        current_index = input_index

        # Right to left through rotors
        for rotor in reversed(self.rotors):
            current_index = rotor.apply_permutation(current_index, rotor.get_offset())

        # Reflector
        current_index = (ord(REFLECTOR_PERMUTATION[current_index]) - ord('A'))

        # Left to right back through rotors
        for rotor in self.rotors:
            current_index = rotor.apply_permutation(current_index, rotor.get_offset(), reverse=True)

        encrypted_letter = chr(current_index + ord('A'))
        self.lamps_state[encrypted_letter] = True

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
        rotor = self.rotors[index]
        offset = rotor.get_offset()
        return chr(ord('A') + offset)

    def advance_rotors(self):
        if self.rotors[2].advance():
            if self.rotors[1].advance():
                self.rotors[0].advance()

def enigma():
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

if __name__ == "__main__":
    enigma()