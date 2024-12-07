from EnigmaConstants import ROTOR_PERMUTATIONS
from EnigmaRotor import EnigmaRotor

class EnigmaModel:
    def __init__(self):
        self._views = []
        self.rotors = []
        for permutation in ROTOR_PERMUTATIONS:
            rotor = EnigmaRotor(permutation)
            self.rotors.append(rotor)

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
        rotor = self.rotors[index]
        rotor.advance()
        self.update()

    def get_rotor_letter(self, index):
        rotor = self.rotors[index]
        offset = rotor.get_offset()
        permutation = rotor.get_permutation()
        letter_index = (offset + 0) % 26  # Adjust for the rotor offset
        return permutation[letter_index]

    def advance_rotors(self):
        for i in range(len(self.rotors) - 1, 0, -1):
            rotor = self.rotors[i]
            if rotor.advance():
                self.rotors[i - 1].advance()