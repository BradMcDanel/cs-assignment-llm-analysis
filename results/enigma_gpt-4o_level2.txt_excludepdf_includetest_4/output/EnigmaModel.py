class EnigmaModel:

    def __init__(self):
        """Creates a new EnigmaModel with no views."""
        self._views = []
        self._key_states = {}
        self._lamp_states = {}
        self._rotors = [EnigmaRotor(ROTOR_PERMUTATIONS[i]) for i in range(3)]
        self._reflector_permutation = "IXUHFEZDAOMTKQJWNSRLCYPBVG"

    def add_view(self, view):
        """Adds a view to this model."""
        self._views.append(view)

    def update(self):
        """Sends an update request to all the views."""
        for view in self._views:
            view.update()

    def encrypt_letter(self, index):
        # Forward pass through the rotors
        for rotor in self._rotors:
            index = apply_permutation(index, rotor.get_permutation(), rotor.get_offset())
        # Pass through the reflector
        index = apply_permutation(index, self._reflector_permutation, 0)
        # Backward pass through the rotors
        for rotor in reversed(self._rotors):
            index = apply_permutation(index, rotor.get_inverse_permutation(), rotor.get_offset())
        return index

    def advance_rotors(self):
        # Advance the fast rotor and check for carry
        carry = self._rotors[0].advance()
        if carry:
            # Advance the medium rotor and check for carry
            carry = self._rotors[1].advance()
            if carry:
                # Advance the slow rotor
                self._rotors[2].advance()

    def key_pressed(self, letter):
        self._key_states[letter] = True
        # Advance the rotors before encryption
        self.advance_rotors()
        # Encrypt the letter
        index = ord(letter) - ord('A')
        encrypted_index = self.encrypt_letter(index)
        encrypted_letter = chr(ord('A') + encrypted_index)
        self._lamp_states[encrypted_letter] = True
        self.update()

    def key_released(self, letter):
        self._key_states[letter] = False
        for lamp in self._lamp_states:
            self._lamp_states[lamp] = False
        self.update()

    def is_key_down(self, letter):
        return self._key_states.get(letter, False)

    def is_lamp_on(self, letter):
        return self._lamp_states.get(letter, False)

    def rotor_clicked(self, index):
        self._rotors[index].advance()
        self.update()

    def get_rotor_letter(self, index):
        offset = self._rotors[index].get_offset()
        return chr((ord('A') + offset) % 26)

def enigma():
    """Runs the Enigma simulator."""
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

# Startup code
if __name__ == "__main__":
    enigma()