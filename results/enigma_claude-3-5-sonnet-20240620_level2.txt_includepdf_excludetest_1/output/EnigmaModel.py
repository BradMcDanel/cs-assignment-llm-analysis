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

    def encrypt(self, index, forward=True):
        permutation = self.permutation if forward else self.inverse_permutation
        shifted_index = (index + self.offset) % 26
        encrypted_index = ord(permutation[shifted_index]) - ord('A')
        return (encrypted_index - self.offset) % 26

class EnigmaModel:
    def __init__(self):
        self._views = []
        self.rotors = [EnigmaRotor(perm) for perm in ROTOR_PERMUTATIONS]
        self.reflector = EnigmaRotor(REFLECTOR_PERMUTATION)
        self.key_state = {letter: False for letter in ALPHABET}
        self.lamp_state = {letter: False for letter in ALPHABET}

    def add_view(self, view):
        self._views.append(view)

    def update(self):
        for view in self._views:
            view.update()

    def is_key_down(self, letter):
        return self.key_state[letter]

    def is_lamp_on(self, letter):
        return self.lamp_state[letter]

    def key_pressed(self, letter):
        self.key_state[letter] = True
        self.advance_rotors()
        encrypted = self.encrypt(letter)
        self.lamp_state = {l: l == encrypted for l in ALPHABET}
        self.update()

    def key_released(self, letter):
        self.key_state[letter] = False
        self.lamp_state = {l: False for l in ALPHABET}
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
            index = rotor.encrypt(index)
        
        # Through reflector
        index = self.reflector.encrypt(index)
        
        # Left to right through rotors  
        for rotor in self.rotors:
            index = rotor.encrypt(index, forward=False)
        
        return chr(index + ord('A'))

def enigma():
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

if __name__ == "__main__":
    enigma()