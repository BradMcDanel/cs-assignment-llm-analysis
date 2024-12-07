from EnigmaView import EnigmaView
from EnigmaConstants import ALPHABET, N_ROTORS, ROTOR_PERMUTATIONS, REFLECTOR_PERMUTATION
from EnigmaRotor import EnigmaRotor, apply_permutation

class EnigmaModel:
    def __init__(self):
        """Creates a new EnigmaModel with no views."""
        self._views = []
        self._keys_down = {letter: False for letter in ALPHABET}
        self._lamps_on = {letter: False for letter in ALPHABET}
        self._rotors = [EnigmaRotor(ROTOR_PERMUTATIONS[i]) for i in range(N_ROTORS)]

    def add_view(self, view):
        """Adds a view to this model."""
        self._views.append(view)

    def update(self):
        """Sends an update request to all the views."""
        for view in self._views:
            view.update()

    def is_key_down(self, letter):
        return self._keys_down[letter]

    def is_lamp_on(self, letter):
        return self._lamps_on[letter]

    def key_pressed(self, letter):
        self._keys_down[letter] = True
        self._advance_rotors()
        encrypted_letter = self._encrypt(letter)
        self._lamps_on[encrypted_letter] = True
        self.update()

    def key_released(self, letter):
        self._keys_down[letter] = False
        for lamp in ALPHABET:
            self._lamps_on[lamp] = False
        self.update()

    def get_rotor_letter(self, index):
        return self._rotors[index].get_visible_letter()

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
        # Right to left through rotors
        index = ALPHABET.index(letter)
        for rotor in reversed(self._rotors):
            index = apply_permutation(index, rotor.get_permutation(), rotor.get_offset())
        
        # Through reflector
        index = ALPHABET.index(REFLECTOR_PERMUTATION[index])
        
        # Left to right through rotors
        for rotor in self._rotors:
            index = apply_permutation(index, rotor.get_inverse_permutation(), rotor.get_offset())
        
        return ALPHABET[index]

def enigma():
    """Runs the Enigma simulator."""
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

# Startup code
if __name__ == "__main__":
    enigma()