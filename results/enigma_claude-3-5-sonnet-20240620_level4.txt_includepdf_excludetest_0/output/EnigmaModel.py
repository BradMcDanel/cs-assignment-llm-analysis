from EnigmaView import EnigmaView
from EnigmaConstants import ALPHABET, N_ROTORS, ROTOR_PERMUTATIONS, REFLECTOR_PERMUTATION

class EnigmaRotor:
    def __init__(self, permutation):
        self._permutation = permutation
        self._inverse_permutation = self._invert_permutation(permutation)
        self._offset = 0

    def _invert_permutation(self, permutation):
        return ''.join(sorted(permutation, key=lambda c: permutation.index(c)))

    def get_offset(self):
        return self._offset

    def get_permutation(self):
        return self._permutation

    def advance(self):
        self._offset = (self._offset + 1) % 26
        return self._offset == 0

    def apply_forward(self, index):
        return self._apply_permutation(index, self._permutation)

    def apply_backward(self, index):
        return self._apply_permutation(index, self._inverse_permutation)

    def _apply_permutation(self, index, permutation):
        shifted_index = (index + self._offset) % 26
        new_index = ALPHABET.index(permutation[shifted_index])
        return (new_index - self._offset) % 26

class EnigmaModel:
    def __init__(self):
        self._views = []
        self._keys_down = {letter: False for letter in ALPHABET}
        self._lamps_on = {letter: False for letter in ALPHABET}
        self._rotors = [EnigmaRotor(perm) for perm in ROTOR_PERMUTATIONS]
        self._reflector = EnigmaRotor(REFLECTOR_PERMUTATION)

    def add_view(self, view):
        self._views.append(view)

    def update(self):
        for view in self._views:
            view.update()

    def is_key_down(self, letter):
        return self._keys_down[letter]

    def is_lamp_on(self, letter):
        return self._lamps_on[letter]

    def key_pressed(self, letter):
        self._keys_down[letter] = True
        self._advance_rotors()
        encrypted_letter = self._encrypt(letter)
        self._lamps_on[encrypted_letter] = True
        self.update()

    def key_released(self, letter):
        self._keys_down[letter] = False
        encrypted_letter = self._encrypt(letter)
        self._lamps_on[encrypted_letter] = False
        self.update()

    def get_rotor_letter(self, index):
        return ALPHABET[self._rotors[index].get_offset()]

    def rotor_clicked(self, index):
        self._rotors[index].advance()
        self.update()

    def _advance_rotors(self):
        if self._rotors[2].advance():
            if self._rotors[1].advance():
                self._rotors[0].advance()

    def _encrypt(self, letter):
        index = ALPHABET.index(letter)
        
        # Right to left through rotors
        for rotor in reversed(self._rotors):
            index = rotor.apply_forward(index)
        
        # Through reflector
        index = self._reflector.apply_forward(index)
        
        # Left to right through rotors
        for rotor in self._rotors:
            index = rotor.apply_backward(index)
        
        return ALPHABET[index]

def enigma():
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

if __name__ == "__main__":
    enigma()