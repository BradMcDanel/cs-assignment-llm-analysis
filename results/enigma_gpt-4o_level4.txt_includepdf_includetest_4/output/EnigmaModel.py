from EnigmaView import EnigmaView
from EnigmaConstants import ALPHABET, N_ROTORS, ROTOR_PERMUTATIONS, REFLECTOR_PERMUTATION

class EnigmaRotor:
    def __init__(self, permutation):
        self.permutation = permutation
        self.inverse_permutation = self._invert_key(permutation)
        self.offset = 0

    def get_offset(self):
        return self.offset

    def get_permutation(self):
        return self.permutation

    def advance(self):
        self.offset = (self.offset + 1) % 26
        return self.offset == 0

    def _invert_key(self, key):
        inverse = [''] * 26
        for i, char in enumerate(key):
            inverse[ord(char) - ord('A')] = ALPHABET[i]
        return ''.join(inverse)

class EnigmaModel:
    def __init__(self):
        """Creates a new EnigmaModel with no views."""
        self._views = []
        self.keys_state = {letter: False for letter in ALPHABET}
        self.lamps_state = {letter: False for letter in ALPHABET}
        self.rotors = [EnigmaRotor(ROTOR_PERMUTATIONS[i]) for i in range(N_ROTORS)]

    def add_view(self, view):
        """Adds a view to this model."""
        self._views.append(view)

    def update(self):
        """Sends an update request to all the views."""
        for view in self._views:
            view.update()

    def key_pressed(self, letter):
        self.keys_state[letter] = True
        self.advance_rotors()
        encrypted_index = self.encrypt(letter)
        encrypted_letter = ALPHABET[encrypted_index]
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
        offset = self.rotors[index].get_offset()
        return ALPHABET[offset]

    def advance_rotors(self):
        carry = self.rotors[-1].advance()
        if carry:
            carry = self.rotors[-2].advance()
            if carry:
                self.rotors[-3].advance()

    def encrypt(self, letter):
        index = ALPHABET.index(letter)
        for rotor in reversed(self.rotors):
            index = self.apply_permutation(index, rotor.permutation, rotor.offset)
        index = self.apply_permutation(index, REFLECTOR_PERMUTATION, 0)
        for rotor in self.rotors:
            index = self.apply_permutation(index, rotor.inverse_permutation, rotor.offset)
        return index

    def apply_permutation(self, index, permutation, offset):
        shifted_index = (index + offset) % 26
        char = permutation[shifted_index]
        new_index = (ALPHABET.index(char) - offset) % 26
        return new_index

def enigma():
    """Runs the Enigma simulator."""
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

# Startup code
if __name__ == "__main__":
    enigma()