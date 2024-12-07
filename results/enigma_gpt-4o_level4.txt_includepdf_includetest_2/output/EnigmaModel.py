from EnigmaView import EnigmaView
from EnigmaConstants import ALPHABET, N_ROTORS, ROTOR_PERMUTATIONS, REFLECTOR_PERMUTATION

class EnigmaRotor:
    """Class representing a single Enigma rotor."""

    def __init__(self, permutation):
        self.permutation = permutation
        self.inverse_permutation = self.invert_permutation(permutation)
        self.offset = 0

    def invert_permutation(self, permutation):
        """Creates the inverse permutation."""
        inverse = [''] * len(permutation)
        for i, char in enumerate(permutation):
            inverse[ord(char) - ord('A')] = ALPHABET[i]
        return ''.join(inverse)

    def apply_permutation(self, index, forward=True):
        """Applies the permutation with the current offset."""
        shifted_index = (index + self.offset) % 26
        if forward:
            letter = self.permutation[shifted_index]
        else:
            letter = self.inverse_permutation[shifted_index]
        return (ord(letter) - ord('A') - self.offset) % 26

    def advance(self):
        """Advances the rotor and returns True if a full revolution is completed."""
        self.offset = (self.offset + 1) % 26
        return self.offset == 0

    def get_letter(self):
        """Returns the current letter visible on the rotor."""
        return ALPHABET[self.offset]


class EnigmaModel:
    """Class representing the entire Enigma machine model."""

    def __init__(self):
        """Initializes the Enigma model with three rotors."""
        self._views = []
        self.keys_down = {letter: False for letter in ALPHABET}
        self.lamps_on = {letter: False for letter in ALPHABET}
        self.rotors = [EnigmaRotor(ROTOR_PERMUTATIONS[i]) for i in range(N_ROTORS)]

    def add_view(self, view):
        """Adds a view to this model."""
        self._views.append(view)

    def update(self):
        """Sends an update request to all the views."""
        for view in self._views:
            view.update()

    def key_pressed(self, letter):
        self.keys_down[letter] = True
        self.encrypt(letter)
        self.update()

    def key_released(self, letter):
        self.keys_down[letter] = False
        for lamp in self.lamps_on:
            self.lamps_on[lamp] = False
        self.update()

    def is_key_down(self, letter):
        return self.keys_down[letter]

    def is_lamp_on(self, letter):
        return self.lamps_on[letter]

    def rotor_clicked(self, index):
        self.rotors[index].advance()
        self.update()

    def get_rotor_letter(self, index):
        return self.rotors[index].get_letter()

    def encrypt(self, letter):
        """Encrypts the given letter using the rotor settings and lights the corresponding lamp."""
        index = ALPHABET.index(letter)
        # Advance the fast rotor
        carry = self.rotors[-1].advance()
        if carry:
            carry = self.rotors[-2].advance()
            if carry:
                self.rotors[-3].advance()
        
        # Forward pass through the rotors
        for rotor in reversed(self.rotors):
            index = rotor.apply_permutation(index, forward=True)
        
        # Reflector
        reflected_letter = REFLECTOR_PERMUTATION[index]
        index = ALPHABET.index(reflected_letter)
        
        # Backward pass through the rotors
        for rotor in self.rotors:
            index = rotor.apply_permutation(index, forward=False)
        
        # Light up the lamp
        encrypted_letter = ALPHABET[index]
        self.lamps_on[encrypted_letter] = True


def enigma():
    """Runs the Enigma simulator."""
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)


# Startup code
if __name__ == "__main__":
    enigma()