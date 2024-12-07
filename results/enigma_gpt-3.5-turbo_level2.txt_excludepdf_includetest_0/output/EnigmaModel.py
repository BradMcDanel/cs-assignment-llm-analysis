from EnigmaConstants import ROTOR_PERMUTATIONS, REFLECTOR_PERMUTATION
from EnigmaRotor import EnigmaRotor

def invert_key(key):
    return key[::-1]

def apply_permutation(index, permutation, offset):
    shifted_index = (index + offset) % 26
    new_char = permutation[shifted_index]
    new_index = (ord(new_char) - ord('A') - offset) % 26
    return new_index

class EnigmaModel:
    
    def __init__(self):
        self._views = []
        self.rotors = [EnigmaRotor(perm) for perm in ROTOR_PERMUTATIONS]
        self.reflector_permutation = REFLECTOR_PERMUTATION
    
    def add_view(self, view):
        self._views.append(view)
    
    def update(self):
        for view in self._views:
            view.update()
    
    def key_pressed(self, letter):
        # Implement encryption path through rotors
        pass
    
    def key_released(self, letter):
        self.update()
    
    def is_key_down(self, letter):
        return False
    
    def is_lamp_on(self, letter):
        return False
    
    def rotor_clicked(self, index):
        if 0 <= index < len(self.rotors):
            rotor = self.rotors[index]
            rotor.advance()
        self.update()
    
    def get_rotor_letter(self, index):
        if 0 <= index < len(self.rotors):
            rotor = self.rotors[index]
            offset = rotor.get_offset()
            permutation = rotor.get_permutation()
            return permutation[offset]
        return "A"

def enigma():
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

if __name__ == "__main__":
    enigma()