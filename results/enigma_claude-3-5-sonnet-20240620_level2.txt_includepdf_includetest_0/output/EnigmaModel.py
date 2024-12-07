from EnigmaView import EnigmaView
from EnigmaConstants import ALPHABET, N_ROTORS, ROTOR_PERMUTATIONS, REFLECTOR_PERMUTATION

class EnigmaRotor:
    def __init__(self, permutation):
        self.permutation = permutation
        self.inverse_permutation = self.invert_key(permutation)
        self.offset = 0
    
    def invert_key(self, key):
        return ''.join(sorted(ALPHABET, key=lambda c: key.index(c)))
    
    def advance(self):
        self.offset = (self.offset + 1) % 26
        return self.offset == 0
    
    def get_offset(self):
        return self.offset
    
    def get_permutation(self):
        return self.permutation

class EnigmaModel:

    def __init__(self):
        self._views = []
        self._keys_down = {letter: False for letter in ALPHABET}
        self._lamps_on = {letter: False for letter in ALPHABET}
        self._rotors = [EnigmaRotor(perm) for perm in ROTOR_PERMUTATIONS]
        self._reflector = REFLECTOR_PERMUTATION

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
        encrypted = self._encrypt(letter)
        self._lamps_on = {l: l == encrypted for l in ALPHABET}
        self.update()

    def key_released(self, letter):
        self._keys_down[letter] = False
        self._lamps_on = {l: False for l in ALPHABET}
        self.update()

    def get_rotor_letter(self, index):
        return ALPHABET[self._rotors[index].get_offset()]

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

    def _encrypt(self, letter):
        index = ALPHABET.index(letter)
        
        # Right to left through rotors
        for rotor in reversed(self._rotors):
            index = self._apply_rotor(index, rotor.get_permutation(), rotor.get_offset())
        
        # Reflector
        index = ALPHABET.index(self._reflector[index])
        
        # Left to right through rotors
        for rotor in self._rotors:
            index = self._apply_rotor(index, rotor.inverse_permutation, -rotor.get_offset())
        
        return ALPHABET[index]

    def _apply_rotor(self, index, permutation, offset):
        index = (index + offset) % 26
        letter = permutation[index]
        return (ALPHABET.index(letter) - offset) % 26

def enigma():
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

if __name__ == "__main__":
    enigma()