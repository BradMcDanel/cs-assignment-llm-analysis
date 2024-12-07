from EnigmaView import EnigmaView
from EnigmaConstants import ALPHABET, ROTOR_PERMUTATIONS, REFLECTOR_PERMUTATION

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

    def advance(self):
        self.offset = (self.offset + 1) % 26
        return self.offset == 0

    def get_offset(self):
        return self.offset

    def get_permutation(self):
        return self.permutation

    def get_inverse_permutation(self):
        return self.inverse_permutation

def apply_permutation(index, permutation, offset):
    shifted_index = (index + offset) % 26
    letter = permutation[shifted_index]
    new_index = (ord(letter) - ord('A') - offset) % 26
    return new_index

class EnigmaModel:
    def __init__(self):
        """Creates a new EnigmaModel with no views."""
        self._views = []
        self.keys_down = {}
        self.lamps_on = {}
        self.rotors = [EnigmaRotor(ROTOR_PERMUTATIONS[i]) for i in range(3)]
        for letter in ALPHABET:
            self.keys_down[letter] = False
            self.lamps_on[letter] = False

    def add_view(self, view):
        """Adds a view to this model."""
        self._views.append(view)

    def update(self):
        """Sends an update request to all the views."""
        for view in self._views:
            view.update()

    def is_key_down(self, letter):
        return self.keys_down.get(letter, False)

    def is_lamp_on(self, letter):
        return self.lamps_on.get(letter, False)

    def key_pressed(self, letter):
        self.keys_down[letter] = True
        self.advance_rotors()
        lamp_index = self.encrypt(letter)
        lamp_letter = ALPHABET[lamp_index]
        self.lamps_on[lamp_letter] = True
        self.update()

    def key_released(self, letter):
        self.keys_down[letter] = False
        for lamp in self.lamps_on:
            self.lamps_on[lamp] = False
        self.update()

    def get_rotor_letter(self, index):
        offset = self.rotors[index].get_offset()
        return ALPHABET[offset]

    def rotor_clicked(self, index):
        self.rotors[index].advance()
        self.update()

    def advance_rotors(self):
        if self.rotors[2].advance():
            if self.rotors[1].advance():
                self.rotors[0].advance()

    def encrypt(self, letter):
        index = ord(letter) - ord('A')
        for rotor in reversed(self.rotors):
            index = apply_permutation(index, rotor.get_permutation(), rotor.get_offset())
        index = apply_permutation(index, REFLECTOR_PERMUTATION, 0)
        for rotor in self.rotors:
            index = apply_permutation(index, rotor.get_inverse_permutation(), rotor.get_offset())
        return index

def enigma():
    """Runs the Enigma simulator."""
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

# Startup code
if __name__ == "__main__":
    enigma()