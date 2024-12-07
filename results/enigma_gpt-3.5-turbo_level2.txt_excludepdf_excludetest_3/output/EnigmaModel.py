from EnigmaRotor import EnigmaRotor

ROTOR_PERMUTATIONS = [
    "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
    "AJDKSIRUXBLHWTMCQGZNPYFVOE",
    "BDFHJLCPRTXVZNYEIWGAKMUSQO"
]

class EnigmaModel:
    def __init__(self):
        self._views = []
        self.rotors = [EnigmaRotor(perm) for perm in ROTOR_PERMUTATIONS]
    
    def add_view(self, view):
        self._views.append(view)
    
    def update(self):
        for view in self._views:
            view.update()
    
    def key_pressed(self, letter):
        self.advance_rotors()
        self.update()
    
    def key_released(self, letter):
        self.update()
    
    def is_key_down(self, letter):
        return False
    
    def is_lamp_on(self, letter):
        return False
    
    def rotor_clicked(self, index):
        self.rotors[index].advance()
        self.update()
    
    def get_rotor_letter(self, index):
        rotor = self.rotors[index]
        offset = rotor.get_offset()
        permutation = rotor.get_permutation()
        return permutation[offset]
    
    def advance_rotors(self):
        for i in range(len(self.rotors) - 1, 0, -1):
            if self.rotors[i].advance():
                self.rotors[i - 1].advance()