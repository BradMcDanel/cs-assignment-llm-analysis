# Your EnigmaModel class implementation for the Enigma machine simulation.

class EnigmaRotor:
    def __init__(self, permutation):
        self.permutation = permutation
        self.offset = 0

    def get_offset(self):
        return self.offset

    def get_permutation(self):
        return self.permutation

    def advance(self):
        self.offset = (self.offset + 1) % 26
        return self.offset == 0

class EnigmaModel:
    def __init__(self):
        self._views = []
        self.rotors = [EnigmaRotor(ROTOR_PERMUTATIONS[0]),
                       EnigmaRotor(ROTOR_PERMUTATIONS[1]),
                       EnigmaRotor(ROTOR_PERMUTATIONS[2])]

    def add_view(self, view):
        self._views.append(view)

    def update(self):
        for view in self._views:
            view.update()

    def key_pressed(self, letter):
        self.update()
        # Add encryption logic here

    def key_released(self, letter):
        self.update()
        # Add encryption logic here

    def is_key_down(self, letter):
        # Check if the key is currently pressed
        return False

    def is_lamp_on(self, letter):
        # Check if the lamp for the letter is currently on
        return False

    def rotor_clicked(self, index):
        rotor = self.rotors[index]
        if rotor.advance():
            # Propagate carry to the next rotor
            if index < 2:
                self.rotors[index + 1].advance()
        self.update()

    def get_rotor_letter(self, index):
        rotor = self.rotors[index]
        offset = rotor.get_offset()
        permutation = rotor.get_permutation()
        return permutation[offset]

def enigma():
    """Runs the Enigma simulator."""
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

# Startup code

if __name__ == "__main__":
    enigma()