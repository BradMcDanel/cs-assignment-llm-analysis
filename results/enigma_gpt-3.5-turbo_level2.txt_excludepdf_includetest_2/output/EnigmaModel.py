from EnigmaRotor import EnigmaRotor

class EnigmaModel:
    def __init__(self):
        self._views = []
        self.rotors = [EnigmaRotor(ROTOR_PERMUTATIONS[i]) for i in range(3)]

    def add_view(self, view):
        self._views.append(view)

    def update(self):
        for view in self._views:
            view.update()

    def key_pressed(self, letter):
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
        letter_index = (offset) % 26
        return chr(ord('A') + letter_index)