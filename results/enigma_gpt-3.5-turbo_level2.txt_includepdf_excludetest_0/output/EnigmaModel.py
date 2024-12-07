# Your EnigmaModel class implementation here

class EnigmaModel:
    def __init__(self):
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
        # Add code to respond when the key is pressed
        self.update()

    def key_released(self, letter):
        # Add code to respond when the key is released
        self.update()

    def get_rotor_letter(self, index):
        return "A"

    def rotor_clicked(self, index):
        # Add code to respond when the rotor is clicked
        self.update()

def enigma():
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

if __name__ == "__main__":
    enigma()