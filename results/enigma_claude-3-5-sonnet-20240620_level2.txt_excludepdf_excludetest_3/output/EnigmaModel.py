from EnigmaView import EnigmaView
from EnigmaRotor import EnigmaRotor
from EnigmaConstants import ROTOR_PERMUTATIONS, REFLECTOR_PERMUTATION

class EnigmaModel:

    def __init__(self):
        """Creates a new EnigmaModel with no views."""
        self._views = []
        self._key_state = {chr(65+i): False for i in range(26)}  # Initialize all keys as up
        self._lamp_state = {chr(65+i): False for i in range(26)}  # Initialize all lamps as off
        self._rotors = [EnigmaRotor(perm) for perm in ROTOR_PERMUTATIONS]
        self._reflector = EnigmaRotor(REFLECTOR_PERMUTATION)

    def key_pressed(self, letter):
        self._key_state[letter] = True
        
        # Advance rotors
        self.advance_rotors()
        
        # Full encryption path
        index = ord(letter) - 65
        
        # Forward through rotors
        for rotor in reversed(self._rotors):
            index = rotor.apply_forward(index)
        
        # Through reflector
        index = self._reflector.apply_forward(index)
        
        # Backward through rotors
        for rotor in self._rotors:
            index = rotor.apply_backward(index)
        
        encrypted_letter = chr(index + 65)
        self._lamp_state[encrypted_letter] = True
        self.update()

    def advance_rotors(self):
        # Always advance the fast rotor
        carry = self._rotors[2].advance()
        
        # If there's a