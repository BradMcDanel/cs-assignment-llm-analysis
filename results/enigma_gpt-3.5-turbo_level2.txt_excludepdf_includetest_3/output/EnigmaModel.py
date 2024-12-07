from EnigmaRotor import EnigmaRotor

class EnigmaModel:
    def __init__(self):
        self._views = []
        self.rotors = []
        for perm in ROTOR_PERMUTATIONS:
            rotor = EnigmaRotor(perm)
            self.rotors.append(rotor)

    def add_view(self, view):
        self._views.append(view)

    def update(self):
        for view in self._views:
            view.update()

    def key_pressed(self, letter):
        for rotor in self.rotors:
            if rotor.advance():
                # Carry to the next rotor
                idx = self.rotors.index(rotor)
                if idx < len(self.rotors) - 1:
                    self.rotors[idx + 1].advance()
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
        letter_idx = (offset) % 26
        return permutation[letter_idx]