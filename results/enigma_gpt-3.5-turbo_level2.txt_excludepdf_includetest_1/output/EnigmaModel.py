from EnigmaRotor import EnigmaRotor

class EnigmaModel:
    def __init__(self):
        self._views = []
        self.rotors = [EnigmaRotor(ROTOR_PERMUTATIONS[0]), 
                       EnigmaRotor(ROTOR_PERMUTATIONS[1]), 
                       EnigmaRotor(ROTOR_PERMUTATIONS[2])]

    def key_pressed(self, letter):
        # Implement encryption path
        pass

    def key_released(self, letter):
        # Implement encryption path
        pass

    def invert_key(self, key):
        return key[::-1]