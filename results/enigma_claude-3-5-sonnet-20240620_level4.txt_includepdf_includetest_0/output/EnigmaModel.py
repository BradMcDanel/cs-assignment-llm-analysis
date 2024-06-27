from EnigmaView import EnigmaView
from EnigmaConstants import ALPHABET, N_ROTORS, ROTOR_PERMUTATIONS, REFLECTOR_PERMUTATION

class EnigmaRotor:
    def __init__(self, permutation):
        self.permutation = permutation
        self.inverse_permutation = self._invert_permutation(permutation)
        self.offset = 0

    def _invert_permutation(self, permutation):
        return ''.join(sorted(permutation, key=lambda c: permutation.index(c)))

    def advance(self):
        self.offset = (self.offset + 1) % 26
        return self.offset == 0

    def encode(self, char, reverse=False):
        if reverse:
            perm = self.inverse_permutation
        else:
            perm = self.permutation
        index = (ALPHABET.index(char) + self.offset) % 26
        encoded = perm[index]
        return ALPHABET[(ALPHABET.index(encoded) - self.offset) % 26]

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
        encoded = self._encode(letter)
        self._lamps_on = {l: l == encoded for l in ALPHABET}
        self.update()

    def key_released(self, letter):
        self._keys_down[letter] = False
        self._lamps_on = {l: False for l in ALPHABET}
        self.update()

    def get_rotor_letter(self, index):
        return ALPHABET[self._rotors[index].offset]

    def rotor_clicked(self, index):
        self._rotors[index].advance()
        self.update()

    def _advance_rotors(self):
        carry = True
        for rotor in reversed(self._rotors):
            if carry:
                carry = rotor.advance()
            else:
                break

    def _encode(self, letter):
        # Right to left through rotors
        for rotor in reversed(self._rotors):
            letter = rotor.encode(letter)
        
        # Through reflector
        letter = self._reflector.encode(letter)
        
        # Left to right through rotors
        for rotor in self._rotors:
            letter = rotor.encode(letter, reverse=True)
        
        return letter

def enigma():
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

if __name__ == "__main__":
    enigma()