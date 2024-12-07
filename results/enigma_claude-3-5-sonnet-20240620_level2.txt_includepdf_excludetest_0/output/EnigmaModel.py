from EnigmaView import EnigmaView
from EnigmaConstants import *

class EnigmaRotor:
    def __init__(self, permutation):
        self.permutation = permutation
        self.inverse_permutation = self.invert_key(permutation)
        self.offset = 0
    
    def invert_key(self, key):
        inverse = [''] * 26
        for i, letter in enumerate(key):
            inverse[ord(letter) - ord('A')] = chr(i + ord('A'))
        return ''.join(inverse)
    
    def advance(self):
        self.offset = (self.offset + 1) % 26
        return self.offset == 0

    def apply_permutation(self, index, forward=True):
        perm = self.permutation if forward else self.inverse_permutation
        shifted = (index + self.offset) % 26
        new_index = ord(perm[shifted]) - ord('A')
        return (new_index - self.offset) % 26

class EnigmaModel:
    def __init__(self):
        self._views = []
        self.keys_down = {letter: False for letter in ALPHABET}
        self.lamps_on = {letter: False for letter in ALPHABET}
        self.rotors = [EnigmaRotor(perm) for perm in ROTOR_PERMUTATIONS]
        self.reflector = EnigmaRotor(REFLECTOR_PERMUTATION)

    def add_view(self, view):
        self._views.append(view)

    def update(self):
        for view in self._views:
            view.update()

    def is_key_down(self, letter):
        return self.keys_down[letter]

    def is_lamp_on(self, letter):
        return self.lamps_on[letter]

    def key_pressed(self, letter):
        self.keys_down[letter] = True
        self.advance_rotors()
        encrypted = self.encrypt(letter)
        self.lamps_on[encrypted] = True
        self.update()

    def key_released(self, letter):
        self.keys_down[letter] = False
        encrypted = self.encrypt(letter)
        self.lamps_on[encrypted] = False
        self.update()

    def get_rotor_letter(self, index):
        return chr((self.rotors[index].offset + ord('A')) % 26)

    def rotor_clicked(self, index):
        self.rotors[index].advance()
        self.update()

    def advance_rotors(self):
        if self.rotors[2].advance():
            if self.rotors[1].advance():
                self.rotors[0].advance()

    def encrypt(self, letter):
        index = ord(letter) - ord('A')
        
        # Right to left through rotors
        for rotor in reversed(self.rotors):
            index = rotor.apply_permutation(index)
        
        # Through reflector
        index = self.reflector.apply_permutation(index)
        
        # Left to right through rotors
        for rotor in self.rotors:
            index = rotor.apply_permutation(index, forward=False)
        
        return chr(index + ord('A'))

def enigma():
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

if __name__ == "__main__":
    enigma()