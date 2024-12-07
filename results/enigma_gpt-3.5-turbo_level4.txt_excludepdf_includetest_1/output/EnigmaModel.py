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
        self.update()

    def key_released(self, letter):
        self.update()

    def is_key_down(self, letter):
        return False

    def is_lamp_on(self, letter):
        return False

    def rotor_clicked(self, index):
        self.update()

    def get_rotor_letter(self, index):
        return "A"

def enigma():
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

if __name__ == "__main__":
    enigma()