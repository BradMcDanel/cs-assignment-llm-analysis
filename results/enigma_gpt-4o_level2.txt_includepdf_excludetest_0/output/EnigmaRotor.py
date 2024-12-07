class EnigmaRotor:
    def __init__(self, permutation):
        """Creates a new rotor with the specified permutation."""
        self._permutation = permutation
        self._offset = 0
        self._inverse_permutation = self.invert_permutation(permutation)

    def get_offset(self):
        """Returns the current offset of the rotor."""
        return self._offset

    def get_permutation(self):
        """Returns the permutation string of the rotor."""
        return self._permutation

    def get_inverse_permutation(self):
        """Returns the inverse permutation string of the rotor."""
        return self._inverse_permutation

    def advance(self):
        """Advances the rotor by one position."""
        self._offset = (self._offset + 1) % 26
        return self._offset == 0  # Return True if a full revolution occurs

    def invert_permutation(self, permutation):
        """Computes the inverse permutation."""
        inverse = [''] * 26
        for i, char in enumerate(permutation):
            inverse[ord(char) - ord('A')] = chr(i + ord('A'))
        return ''.join(inverse)

def apply_permutation(index, permutation, offset):
    """Applies the permutation with the given offset."""
    new_index = (index + offset) % 26
    char = permutation[new_index]
    return (ord(char) - ord('A') - offset) % 26

### EnigmaModel.py ###
from EnigmaView import EnigmaView
from EnigmaRotor import EnigmaRotor, apply_permutation
from EnigmaConstants import ROTOR_PERMUTATIONS, REFLECTOR_PERMUTATION, ALPHABET

class EnigmaModel:

    def __init__(self):
        """Creates a new EnigmaModel with no views."""
        self._views = []
        self._key_states = {letter: False for letter in ALPHABET}
        self._lamp_states = {letter: False for letter in ALPHABET}
        self._rotors = [EnigmaRotor(ROTOR_PERMUTATIONS[i]) for i in range(3)]
        self._reflector_permutation = REFLECTOR_PERMUTATION

    def add_view(self, view):
        """Adds a view to this model."""
        self._views.append(view)

    def update(self):
        """Sends an update request to all the views."""
        for view in self._views:
            view.update()

    def is_key_down(self, letter):
        """Checks if a key is currently pressed."""
        return self._key_states[letter]

    def is_lamp_on(self, letter):
        """Checks if a lamp is currently on."""
        return self._lamp_states[letter]

    def key_pressed(self, letter):
        """Handles key press event."""
        self._key_states[letter] = True
        # Encrypt the letter through all rotors and the reflector
        index = ord(letter) - ord('A')

        # Forward through the rotors
        for rotor in reversed(self._rotors):
            index = apply_permutation(index, rotor.get_permutation(), rotor.get_offset())

        # Through the reflector
        index = (ord(self._reflector_permutation[index]) - ord('A'))

        # Backward through the rotors
        for rotor in self._rotors:
            index = apply_permutation(index, rotor.get_inverse_permutation(), rotor.get_offset())

        encrypted_letter = chr(index + ord('A'))
        self._lamp_states[encrypted_letter] = True
        self.update()

    def key_released(self, letter):
        """Handles key release event."""
        self._key_states[letter] = False
        self._lamp_states = {key: False for key in ALPHABET}  # Turn off all lamps
        self.update()

    def get_rotor_letter(self, index):
        """Returns the letter displayed on the rotor."""
        offset = self._rotors[index].get_offset()
        return chr((ord('A') + offset) % 26 + ord('A'))

    def rotor_clicked(self, index):
        """Handles rotor click event."""
        self._rotors[index].advance()
        self.update()

def enigma():
    """Runs the Enigma simulator."""
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

# Startup code
if __name__ == "__main__":
    enigma()