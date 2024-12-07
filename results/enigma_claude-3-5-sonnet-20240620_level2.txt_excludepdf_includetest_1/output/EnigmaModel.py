from EnigmaView import EnigmaView
from EnigmaConstants import ROTOR_PERMUTATIONS, REFLECTOR_PERMUTATION

class EnigmaRotor:
    def __init__(self, permutation):
        self.permutation = permutation
        self.inverse_permutation = self.invert_key(permutation)
        self.offset = 0
    
    def get_offset(self):
        return self.offset
    
    def get_permutation(self):
        return self.permutation
    
    def advance(self):
        self.offset = (self.offset + 1) % 26
        return self.offset == 0
    
    @staticmethod
    def invert_key(key):
        inverse = [''] * 26
        for i, char in enumerate(key):
            inverse[ord(char) - ord('A')] = chr(i + ord('A'))
        return ''.join(inverse)

def apply_permutation(index, permutation, offset):
    shifted = (index + offset) % 26
    new_index = ord(permutation[shifted]) - ord('A')
    return (new_index - offset) % 26

class EnigmaModel:

    def __init__(self):
        self._views = []
        self.keys_pressed = {chr(i + ord('A')): False for i in range(26)}
        self.lamps_lit = {chr(i + ord('A')): False for i in range(26)}
        self.rotors = [EnigmaRotor(perm) for perm in ROTOR_PERMUTATIONS]

    def add_view(self, view):
        self._views.append(view)

    def update(self):
        for view in self._views:
            view.update()

    def key_pressed(self, letter):
        self.keys_pressed[letter] = True
        self.advance_rotors()
        encrypted = self.encrypt(letter)
        self.lamps_lit[encrypted] = True
        self.update()

    def key_released(self, letter):
        self.keys_pressed[letter] = False
        self.lamps_lit = {k: False for k in self.lamps_lit}
        self.update()

    def is_key_down(self, letter):
        return self.keys_pressed[letter]

    def is_lamp_on(self, letter):
        return self.lamps_lit[letter]

    def rotor_clicked(self, index):
        self.rotors[index].advance()
        self.update()

    def get_rotor_letter(self, index):
        offset = self.rotors[index].get_offset()
        return chr((offset + ord('A')) % 26)

    def advance_rotors(self):
        if self.rotors[2].advance():
            if self.rotors[1].advance():
                self.rotors[0].advance()

    def encrypt(self, letter):
        index = ord(letter) - ord('A')
        
        # Right to left through rotors
        for rotor in reversed(self.rotors):
            index = apply_permutation(index, rotor.get_permutation(), rotor.get_offset())
        
        # Through reflector
        index = apply_permutation(index, REFLECTOR_PERMUTATION, 0)
        
        # Left to right through rotors
        for rotor in self.rotors:
            index = apply_permutation(index, rotor.inverse_permutation, rotor.get_offset())
        
        return chr(index + ord('A'))

def enigma():
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

if __name__ == "__main__":
    enigma()