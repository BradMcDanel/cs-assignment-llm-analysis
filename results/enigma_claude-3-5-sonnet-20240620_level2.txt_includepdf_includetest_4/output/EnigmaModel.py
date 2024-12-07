from EnigmaView import EnigmaView
from EnigmaConstants import ALPHABET, N_ROTORS, ROTOR_PERMUTATIONS, REFLECTOR_PERMUTATION

class EnigmaRotor:
    def __init__(self, permutation):
        self.permutation = permutation
        self.inverse_permutation = self.invert_permutation(permutation)
        self.offset = 0
    
    def invert_permutation(self, perm):
        return ''.join(sorted(perm, key=lambda c: perm.index(c)))
    
    def advance(self):
        self.offset = (self.offset + 1) % 26
        return self.offset == 0
    
    def encode_right_to_left(self, char):
        index = (ALPHABET.index(char) + self.offset) % 26
        encoded = self.permutation[index]
        return ALPHABET[(ALPHABET.index(encoded) - self.offset) % 26]
    
    def encode_left_to_right(self, char):
        index = (ALPHABET.index(char) + self.offset) % 26
        encoded = self.inverse_permutation[index]
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
        if self._rotors[2].advance():
            if self._rotors[1].advance():
                self._rotors[0].advance()

    def _encode(self, letter):
        # Right to left through rotors
        for rotor in reversed(self._rotors):
            letter = rotor.encode_right_to_left(letter)
        
        # Through reflector
        letter = self._reflector.encode_right_to_left(letter)
        
        # Left to right through rotors
        for rotor in self._rotors:
            letter = rotor.encode_left_to_right(letter)
        
        return letter

def enigma():
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

if __name__ == "__main__":
    enigma()