from EnigmaView import EnigmaView
from EnigmaConstants import ALPHABET, N_ROTORS, ROTOR_PERMUTATIONS, REFLECTOR_PERMUTATION
from EnigmaRotor import EnigmaRotor, apply_permutation

class EnigmaModel:
    def __init__(self):
        """Creates a new EnigmaModel with no views."""
        self._views = []
        self._keys = {letter: False for letter in ALPHABET}
        self._lamps = {letter: False for letter in ALPHABET}
        self._rotors = [EnigmaRotor(ROTOR_PERMUTATIONS[i]) for i in range(N_ROTORS)]

    def add_view(self, view):
        """Adds a view to this model."""
        self._views.append(view)

    def update(self):
        """Sends an update request to all the views."""
        for view in self._views:
            view.update()

    def is_key_down(self, letter):
        return self._keys[letter]

    def is_lamp_on(self, letter):
        return self._lamps[letter]

    def key_pressed(self, letter):
        self._keys[letter] = True
        self._advance_rotors()
        encrypted = self._encrypt(letter)
        self._lamps[encrypted] = True
        self.update()

    def key_released(self, letter):
        self._keys[letter] = False
        encrypted = self._encrypt(letter)
        self._lamps[encrypted] = False
        self.update()

    def get_rotor_letter(self, index):
        return chr((self._rotors[index].get_offset() + ord('A')) % 26)

    def rotor_clicked(self, index):
        self._rotors[index].advance()
        self.update()

    def _advance_rotors(self):
        if self._rotors[2].advance():
            if self._rotors[1].advance():
                self._rotors[0].advance()

    def _encrypt(self, letter):
        # Convert letter to index
        index = ord(letter) - ord('A')

        # Right to left through rotors
        for rotor in reversed(self._rotors):
            index = apply_permutation(index, rotor.get_permutation(), rotor.get_offset())

        # Through reflector
        index = apply_permutation(index, REFLECTOR_PERMUTATION, 0)

        # Left to right through rotors
        for rotor in self._rotors:
            index = apply_permutation(index, rotor.get_inverse_permutation(), rotor.get_offset())

        # Convert index back to letter
        return chr(index + ord('A'))

def enigma():
    """Runs the Enigma simulator."""
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

# Startup code
if __name__ == "__main__":
    enigma()