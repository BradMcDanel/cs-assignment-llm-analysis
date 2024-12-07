def apply_permutation(index, permutation, offset):
    """Applies the rotor permutation with offset."""
    shifted_index = (index + offset) % 26
    encrypted_char = permutation[shifted_index]
    return (ALPHABET.index(encrypted_char) - offset) % 26

# Add to EnigmaModel.py
from EnigmaConstants import ALPHABET

class EnigmaModel:

    # Other methods remain unchanged

    def key_pressed(self, letter):
        """Handles the event when a key is pressed."""
        self._key_states[letter] = True
        # Encrypt the letter using the first rotor for now
        index = ALPHABET.index(letter)
        encrypted_index = apply_permutation(index, self._rotors[2].get_permutation(), self._rotors[2].get_offset())
        self._lamp_state = ALPHABET[encrypted_index]
        self.update()

    def is_lamp_on(self, letter):
        """Returns True if the lamp for the letter is on."""
        return letter == getattr(self, '_lamp_state', '')

    def key_released(self, letter):
        """Handles the event when a key is released."""
        self._key_states[letter] = False
        self._lamp_state = ''
        self.update()