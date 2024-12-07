from EnigmaView import EnigmaView
from EnigmaConstants import ROTOR_PERMUTATIONS, REFLECTOR_PERMUTATION

class EnigmaRotor:
    def __init__(self, permutation):
        self.permutation = permutation
        self.offset = 0
        self.inverse_permutation = self.invert_permutation(permutation)
    
    def get_offset(self):
        return self.offset

    def get_permutation(self):
        return self.permutation

    def advance(self):
        self.offset = (self.offset + 1) % 26
        return self.offset == 0  # Return True if a complete revolution is made

    def invert_permutation(self, permutation):
        inverse = [''] * 26
        for i, char in enumerate(permutation):
            inverse[ord(char) - ord('A')] = chr(i + ord('A'))
        return ''.join(inverse)

def apply_permutation(index, permutation, offset):
    shifted_index = (index + offset) % 26
    new_char = permutation[shifted_index]
    new_index = (ord(new_char) - ord('A') - offset) % 26
    return new_index

class EnigmaModel:
    def __init__(self):
        self._views = []
        self.keys_state = {chr(i): False for i in range(ord('A'), ord('Z') + 1)}
        self.lamps_state = {chr(i): False for i in range(ord('A'), ord('Z') + 1)}
        self.rotors = [EnigmaRotor(ROTOR_PERMUTATIONS[i]) for i in range(3)]

    def add_view(self, view):
        self._views.append(view)

    def update(self):
        for view in self._views:
            view.update()

    def key_pressed(self, letter):
        self.keys_state[letter] = True
        self.encrypt_key(letter)
        self.update()

    def key_released(self, letter):
        self.keys_state[letter] = False
        self.lamps_state = {chr(i): False for i in range(ord('A'), ord('Z') + 1)}
        self.update()

    def encrypt_key(self, letter):
        # Advance the fast rotor
        carry = self.rotors[0].advance()
        if carry:
            carry = self.rotors[1].advance()
            if carry:
                self.rotors[2].advance()

        index = ord(letter) - ord('A')
        # Pass through all rotors (right to left)
        for rotor in self.rotors:
            index = apply_permutation(index, rotor.get_permutation(), rotor.get_offset())
        
        # Reflector
        index = apply_permutation(index, REFLECTOR_PERMUTATION, 0)
        
        # Pass through all rotors (left to right)
        for rotor in reversed(self.rotors):
            index = apply_permutation(index, rotor.inverse_permutation, rotor.get_offset())
        
        # Determine the lamp to light up
        encrypted_letter = chr(index + ord('A'))
        self.lamps_state[encrypted_letter] = True

    def is_key_down(self, letter):
        return self.keys_state.get(letter, False)

    def is_lamp_on(self, letter):
        return self.lamps_state.get(letter, False)

    def rotor_clicked(self, index):
        self.rotors[index].advance()
        self.update()

    def get_rotor_letter(self, index):
        rotor = self.rotors[index]
        return chr((rotor.get_offset() + ord('A')) % 26)

def enigma():
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

if __name__ == "__main__":
    enigma()