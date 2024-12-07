from EnigmaView import EnigmaView
from EnigmaRotor import EnigmaRotor
from EnigmaConstants import ROTOR_PERMUTATIONS, REFLECTOR_PERMUTATION

class EnigmaModel:
    def __init__(self):
        """Creates a new EnigmaModel with no views."""
        self._views = []
        self._keys_state = {chr(i): False for i in range(65, 91)}
        self._lamps_state = {chr(i): False for i in range(65, 91)}
        self._rotors = [EnigmaRotor(ROTOR_PERMUTATIONS[i]) for i in range(3)]

    def add_view(self, view):
        """Adds a view to this model."""
        self._views.append(view)

    def update(self):
        """Sends an update request to all the views."""
        for view in self._views:
            view.update()

    def key_pressed(self, letter):
        self._keys_state[letter] = True
        self._lamps_state = {chr(i): False for i in range(65, 91)}  # Reset lamps
        index = ord(letter) - 65
        # Handle rotor advancement
        carry = True
        for rotor in self._rotors:
            if carry:
                carry = rotor.advance()
            else:
                break
        # Encrypt through rotors and reflector
        encrypted_index = self.encrypt(index)
        self._lamps_state[chr(encrypted_index + 65)] = True
        self.update()

    def key_released(self, letter):
        self._keys_state[letter] = False
        self.update()

    def is_key_down(self, letter):
        return self._keys_state[letter]

    def is_lamp_on(self, letter):
        return self._lamps_state[letter]

    def rotor_clicked(self, index):
        self._rotors[index].advance()
        self.update()

    def get_rotor_letter(self, index):
        offset = self._rotors[index].get_offset()
        return chr(offset + 65)

    def encrypt(self, index):
        for rotor in reversed(self._rotors):
            index = rotor.apply_permutation(index, right_to_left=True)
        index = EnigmaRotor.apply_permutation_static(index, REFLECTOR_PERMUTATION, 0)
        for rotor in self._rotors:
            index = rotor.apply_permutation(index, right_to_left=False)
        return index

def enigma():
    """Runs the Enigma simulator."""
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

# Startup code
if __name__ == "__main__":
    enigma()