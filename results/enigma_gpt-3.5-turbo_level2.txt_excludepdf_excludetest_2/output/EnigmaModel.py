from EnigmaRotor import EnigmaRotor

class EnigmaModel:
    def __init__(self):
        self._views = []
        self.rotors = []
        for permutation in ROTOR_PERMUTATIONS:
            self.rotors.append(EnigmaRotor(permutation))

    def add_view(self, view):
        self._views.append(view)

    def update(self):
        for view in self._views:
            view.update()

    def key_pressed(self, letter):
        for rotor in self.rotors:
            if rotor.advance():
                # Carry to the next rotor
                next_rotor_index = self.rotors.index(rotor) + 1
                if next_rotor_index < len(self.rotors):
                    self.rotors[next_rotor_index].advance()
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