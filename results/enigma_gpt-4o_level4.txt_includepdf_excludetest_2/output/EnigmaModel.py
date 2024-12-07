from EnigmaView import EnigmaView
from EnigmaConstants import ALPHABET, ROTOR_PERMUTATIONS, REFLECTOR_PERMUTATION

class EnigmaRotor:
    def __init__(self, permutation):
        self.permutation = permutation
        self.offset = 0
        self.inverse_permutation = self.invert_permutation(permutation)

    def get_offset(self):
        return self.offset

    def get_permutation(self):
        return self.permutation

    def advance(self):
        self.offset = (self.offset + 1) % len(ALPHABET)
        return self.offset == 0  # Return True if we completed a full revolution

    def invert_permutation(self, permutation):
        inverse = [''] * len(permutation)
        for i, char in enumerate(permutation):
            inverse[ALPHABET.index(char)] = ALPHABET[i]
        return ''.join(inverse)

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
        encrypted_index = self.encrypt(ALPHABET.index(letter))
        self.lamps_state[ALPHABET[encrypted_index]] = True
        self.advance_rotors()
        self.update()

    def key_released(self, letter):
        self.keys_state[letter] = False
        self.lamps_state = {letter: False for letter in ALPHABET}
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
        advance_next = self.rotors[2].advance()
        if advance_next:
            advance_next = self.rotors[1].advance()
            if advance_next:
                self.rotors[0].advance()

    def encrypt(self, index):
        # Go through the rotors from right to left
        for rotor in reversed(self.rotors):
            index = self.apply_permutation(index, rotor.get_permutation(), rotor.get_offset())
        # Reflect
        index = self.apply_permutation(index, REFLECTOR_PERMUTATION, 0)
        # Go back through the rotors from left to right
        for rotor in self.rotors:
            index = self.apply_permutation(index, rotor.inverse_permutation, rotor.get_offset())
        return index

    def apply_permutation(self, index, permutation, offset):
        shifted_index = (index + offset) % len(ALPHABET)
        char = permutation[shifted_index]
        return (ALPHABET.index(char) - offset) % len(ALPHABET)

def enigma():
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

if __name__ == "__main__":
    enigma()