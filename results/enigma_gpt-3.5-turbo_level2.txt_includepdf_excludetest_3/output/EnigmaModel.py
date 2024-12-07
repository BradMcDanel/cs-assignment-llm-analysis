# File: EnigmaModel.py

from EnigmaView import EnigmaView

class EnigmaModel:

    def __init__(self):
        """Creates a new EnigmaModel with no views."""
        self._views = []
        self._rotors = []
        self._rotor_positions = [0, 0, 0]  # Initial positions for rotors

    def add_view(self, view):
        """Adds a view to this model."""
        self._views.append(view)

    def update(self):
        """Sends an update request to all the views."""
        for view in self._views:
            view.update()

    def is_key_down(self, letter):
        return False

    def is_lamp_on(self, letter):
        return False

    def key_pressed(self, letter):
        self.advance_rotors()
        self.update()

    def key_released(self, letter):
        self.update()

    def get_rotor_letter(self, index):
        rotor = self._rotors[index]
        offset = self._rotor_positions[index]
        return rotor.get_letter(offset)

    def rotor_clicked(self, index):
        rotor = self._rotors[index]
        rotor.advance()
        self.update()

    def add_rotor(self, rotor):
        self._rotors.append(rotor)

    def advance_rotors(self):
        for i in range(len(self._rotors)):
            if self._rotors[i].should_advance():
                self._rotors[i].advance()
                if i + 1 < len(self._rotors):
                    self._rotors[i + 1].advance()

def enigma():
    """Runs the Enigma simulator."""
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

if __name__ == "__main__":
    enigma()