from EnigmaView import EnigmaView
from EnigmaConstants import ALPHABET, ROTOR_PERMUTATIONS, REFLECTOR_PERMUTATION

class EnigmaRotor:
    def __init__(self, permutation):
        self._permutation = permutation
        self._inverse_permutation = self._invert_permutation(permutation)
        self._offset = 0

    def _invert_permutation(self, permutation):
        inverse = [''] * len(permutation)
        for i, char in enumerate(permutation):
            inverse[ord(char) - ord('A')] = ALPHABET[i]
        return ''.join(inverse)

    def get_offset(self):
        return self._offset

    def get_permutation(self):
        return self._permutation

    def get_inverse_permutation(self):
        return self._inverse_permutation

    def advance(self):
        self._offset = (self._offset + 1) % len(ALPHABET)
        return self._offset == 0

    def map_letter(self, index, forward=True):
        effective_index = (index + self._offset) % len(ALPHABET)
        if forward:
            letter = self._permutation[effective_index]
        else:
            letter = self._inverse_permutation[effective_index]
        return (ord(letter) - ord('A') - self._offset) % len(ALPHABET)

class EnigmaModel:
    def __init__(self):
        self._views = []
        self._keys_down = {letter: False for letter in ALPHABET}
        self._lamps_on = {letter: False for letter in ALPHABET}
        self._rotors = [EnigmaRotor(ROTOR_PERMUTATIONS[i]) for i in range(3)]

    def add_view(self, view):
        self._views.append(view)

    def update(self):
        for view in self._views:
            view.update()

    def key_pressed(self, letter):
        self._keys_down[letter] = True
        self._process_encryption(letter)
        self.update()

    def key_released(self, letter):
        self._keys_down[letter] = False
        self._lamps_on = {l: False for l in ALPHABET}  # Reset lamps when key released
        self.update()

    def is_key_down(self, letter):
        return self._keys_down[letter]

    def is_lamp_on(self, letter):
        return self._lamps_on[letter]

    def rotor_clicked(self, index):
        self._rotors[index].advance()
        self.update()

    def get_rotor_letter(self, index):
        offset = self._rotors[index].get_offset()
        return ALPHABET[offset]

    def _process_encryption(self, letter):
        self._advance_rotors()
        index = ord(letter) - ord('A')

        # Pass through each rotor from right to left
        for rotor in reversed(self._rotors):
            index = rotor.map_letter(index, forward=True)

        # Pass through reflector
        index = (ord(REFLECTOR_PERMUTATION[index]) - ord('A'))

        # Pass back through each rotor from left to right
        for rotor in self._rotors:
            index = rotor.map_letter(index, forward=False)

        # Light the corresponding lamp
        encrypted_letter = ALPHABET[index]
        self._lamps_on[encrypted_letter] = True

    def _advance_rotors(self):
        # Advance the fast rotor
        carry = self._rotors[2].advance()
        
        # Check for carry to medium rotor
        if carry:
            carry = self._rotors[1].advance()
        
        # Check for carry to slow rotor
        if carry:
            self._rotors[0].advance()

def enigma():
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

if __name__ == "__main__":
    enigma()