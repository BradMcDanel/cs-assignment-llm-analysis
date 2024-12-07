from EnigmaView import EnigmaView
from EnigmaConstants import ALPHABET, N_ROTORS, ROTOR_PERMUTATIONS

class EnigmaModel:
    def __init__(self):
        self._rotors = [EnigmaRotor(perm) for perm in ROTOR_PERMUTATIONS]
        self._views = []

    def add_view(self, view):
        self._views.append(view)

    def update(self):
        for view in self._views:
            view.update()

    def is_key_down(self, letter):
        return False

    def is_lamp_on(self, letter):
        return False

    def key_pressed(self, letter):
        # You need to fill in this code
        self.update()

    def key_released(self, letter):
        # You need to fill in this code
        self.update()

    def get_rotor_letter(self, index):
        return self._rotors[index].get_current_letter()

    def rotor_clicked(self, index):
        self._rotors[index].advance()

class EnigmaRotor:
    def __init__(self, permutation):
        self._permutation = permutation
        self._offset = 0

    def get_current_letter(self):
        return self._permutation[self._offset]

    def advance(self):
        self._offset = (self._offset + 1) % 26

def enigma():
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

if __name__ == "__main__":
    enigma()