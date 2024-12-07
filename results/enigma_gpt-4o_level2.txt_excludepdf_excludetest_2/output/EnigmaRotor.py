def apply_permutation(index, permutation, offset):
    shifted_index = (index + offset) % 26
    translated_char = permutation[shifted_index]
    translated_index = (ord(translated_char) - ord('A') - offset) % 26
    return translated_index

def invert_key(key):
    inverted = [''] * 26
    for i, char in enumerate(key):
        inverted[ord(char) - ord('A')] = chr(i + ord('A'))
    return ''.join(inverted)

class EnigmaRotor:
    def __init__(self, permutation):
        self.permutation = permutation
        self.inverse_permutation = invert_key(permutation)
        self.offset = 0
    
    def get_offset(self):
        return self.offset
    
    def get_permutation(self):
        return self.permutation
    
    def get_inverse_permutation(self):
        return self.inverse_permutation
    
    def advance(self):
        self.offset = (self.offset + 1) % 26
        return self.offset == 0

### EnigmaModel.py ###
from EnigmaView import EnigmaView
from EnigmaRotor import EnigmaRotor, apply_permutation
from EnigmaConstants import ROTOR_PERMUTATIONS, REFLECTOR_PERMUTATION

class EnigmaModel:
    def __init__(self):
        """Creates a new EnigmaModel with no views."""
        self._views = []
        self._key_state = {}
        self._lamp_state = {}
        self._rotors = [EnigmaRotor(permutation) for permutation in ROTOR_PERMUTATIONS]
    
    def add_view(self, view):
        """Adds a view to this model."""
        self._views.append(view)
    
    def update(self):
        """Sends an update request to all the views."""
        for view in self._views:
            view.update()
    
    def key_pressed(self, letter):
        self._key_state[letter] = True
        index = ord(letter) - ord('A')
        for rotor in self._rotors:
            index = apply_permutation(index, rotor.get_permutation(), rotor.get_offset())
        index = apply_permutation(index, REFLECTOR_PERMUTATION, 0)
        for rotor in reversed(self._rotors):
            index = apply_permutation(index, rotor.get_inverse_permutation(), rotor.get_offset())
        encrypted_letter = chr(index + ord('A'))
        self._lamp_state[encrypted_letter] = True
        self.update()
    
    def key_released(self, letter):
        self._key_state[letter] = False
        for key in self._lamp_state.keys():
            self._lamp_state[key] = False
        self.update()
    
    def is_key_down(self, letter):
        return self._key_state.get(letter, False)
    
    def is_lamp_on(self, letter):
        return self._lamp_state.get(letter, False)
    
    def rotor_clicked(self, index):
        self._rotors[index].advance()
        self.update()
    
    def get_rotor_letter(self, index):
        rotor = self._rotors[index]
        return chr((ord('A') + rotor.get_offset()) % 26)

def enigma():
    """Runs the Enigma simulator."""
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

# Startup code
if __name__ == "__main__":
    enigma()