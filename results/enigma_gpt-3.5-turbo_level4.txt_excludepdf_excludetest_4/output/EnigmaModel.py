from EnigmaView import EnigmaView

class EnigmaModel:
    def __init__(self):
        self._views = []

    def add_view(self, view):
        self._views.append(view)

    def update(self):
        for view in self._views:
            view.update()

    def key_pressed(self, letter):
        self.update()  # Add code to respond when the key is pressed

    def key_released(self, letter):
        self.update()  # Add code to respond when the key is released

    def is_key_down(self, letter):
        return False  # Add code to return the state of the key

    def is_lamp_on(self, letter):
        return False  # Add code to return the state of the lamp

    def rotor_clicked(self, index):
        self.update()  # Add code to respond when the rotor is clicked

    def get_rotor_letter(self, index):
        return "A"  # In the stub version, all rotors are set to "A"

def enigma():
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

if __name__ == "__main__":
    enigma()