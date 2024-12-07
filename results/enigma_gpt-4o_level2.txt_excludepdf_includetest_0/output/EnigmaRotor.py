class EnigmaRotor:
    def __init__(self, permutation):
        self._permutation = permutation
        self._reverse_permutation = self.invert_permutation(permutation)
        self._offset = 0

    def get_offset(self):
        return self._offset

    def get_permutation(self):
        return self._permutation

    def get_reverse_permutation(self):
        return self._reverse_permutation

    def advance(self):
        self._offset = (self._offset + 1) % 26
        return self._offset == 0

    def invert_permutation(self, permutation):
        inverse = [''] * 26
        for i, char in enumerate(permutation):
            index = ord(char) - ord('A')
            inverse[index] = chr(i + ord('A'))
        return ''.join(inverse)

def apply_permutation(index, permutation, offset):
    shifted_index = (index + offset) % 26
    letter = permutation[shifted_index]
    permuted_index = (ord(letter) - ord('A') - offset) % 26
    return permuted_index

### EnigmaConstants.py ###
REFLECTOR_PERMUTATION = "IXUHFEZDAOMTKQJWNSRLCYPBVG"

### EnigmaModel.py ###
from EnigmaView import EnigmaView
from EnigmaRotor import EnigmaRotor, apply_permutation
from EnigmaConstants import REFLECTOR_PERMUTATION

class EnigmaModel:
    def __init__(self):
        """Creates a new EnigmaModel with no views."""
        self._views = []
        self._keys = {}
        self._lamps = {}
        self._rotors = [EnigmaRotor(permutation) for permutation in [
            "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
            "AJDKSIRUXBLHWTMCQGZNPYFVOE",
            "BDFHJLCPRTXVZNYEIWGAKMUSQO"
        ]]
        self._reflector = REFLECTOR_PERMUTATION

        # Initialize the state of each key and lamp as 'up' (False)
        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            self._keys[letter] = False
            self._lamps[letter] = False

    def add_view(self, view):
        """Adds a view to this model."""
        self._views.append(view)

    def update(self):
        """Sends an update request to all the views."""
        for view in self._views:
            view.update()

    def key_pressed(self, letter):
        self._keys[letter] = True

        # Apply the permutation through the rotors and reflector
        index = ord(letter) - ord('A')
        for rotor in self._rotors:
            index = apply_permutation(index, rotor.get_permutation(), rotor.get_offset())
        
        # Reflector
        index = apply_permutation(index, self._reflector, 0)
        
        # Reverse path through the rotors
        for rotor in reversed(self._rotors):
            index = apply_permutation(index, rotor.get_reverse_permutation(), rotor.get_offset())
        
        permuted_letter = chr(index + ord('A'))
        self._lamps[permuted_letter] = True  # Light corresponding lamp

        self.update()  # Update the view

    def key_released(self, letter):
        self._keys[letter] = False
        
        # Turn off all lamps
        for l in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            self._lamps[l] = False

        self.update()  # Update the view

    def is_key_down(self, letter):
        return self._keys[letter]

    def is_lamp_on(self, letter):
        return self._lamps[letter]

    def rotor_clicked(self, index):
        self._rotors[index].advance()
        self.update()  # Update the view

    def get_rotor_letter(self, index):
        rotor = self._rotors[index]
        offset = rotor.get_offset()
        return chr((ord('A') + offset) % 26 + ord('A'))

def enigma():
    """Runs the Enigma simulator."""
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

# Startup code
if __name__ == "__main__":
    enigma()