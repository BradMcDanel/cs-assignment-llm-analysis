from EnigmaView import EnigmaView
from EnigmaConstants import ROTOR_PERMUTATIONS, REFLECTOR_PERMUTATION
from EnigmaRotor import EnigmaRotor, apply_permutation, invert_key

class EnigmaModel:
    def __init__(self):
        """Creates a new EnigmaModel with no views."""
        self._views = []
        self._keys_down = {chr(65 + i): False for i in range(26)}
        self._lamps_on = {chr(65 + i): False for i in range(26)}
        self._rotors = [
            EnigmaRotor(ROTOR_PERMUTATIONS[2]),  # Fast rotor
            EnigmaRotor(ROTOR_PERMUTATIONS[1]),  # Medium rotor
            EnigmaRotor(ROTOR_PERMUTATIONS[0])   # Slow rotor
        ]
        self._reflector = REFLECTOR_PERMUTATION

    def add_view(self, view):
        """Adds a view to this model."""
        self._views.append(view)

    def update(self):
        """Sends an update request to all the views."""
        for view in self._views:
            view.update()

    def key_pressed(self, letter):
        self._keys_down[letter] = True
        self._advance_rotors()
        encrypted = self._encrypt(letter)
        self._lamps_on[encrypted] = True
        self.update()

    def key_released(self, letter):
        self._keys_down[letter] = False
        encrypted = self._encrypt(letter)
        self._lamps_on[encrypted] = False
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
        return chr((offset + 65) % 26)

    def _advance_rotors(self):
        if self._rotors[0].advance():
            if self._rotors[1].advance():
                self._rotors[2].advance()

    def _encrypt(self, letter):
        index = ord(letter) - 65

        # Right to left through rotors
        for rotor in reversed(self._rotors):
            index = apply_permutation(index, rotor.get_permutation(), rotor.get_offset())

        # Through reflector
        index = apply_permutation(index, self._reflector, 0)

        # Left to right through rotors
        for rotor in self._rotors:
            index = apply_permutation(index, rotor.get_inverse_permutation(), rotor.get_offset())

        return chr(index + 65)

def enigma():
    """Runs the Enigma simulator."""
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

# Startup code
if __name__ == "__main__":
    enigma()