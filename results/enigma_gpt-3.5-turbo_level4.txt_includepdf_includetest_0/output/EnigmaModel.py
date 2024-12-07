from EnigmaView import EnigmaView

class EnigmaModel:

    def __init__(self):
        """Creates a new EnigmaModel with no views."""
        # Implementation omitted for brevity

    def add_view(self, view):
        """Adds a view to this model."""
        # Implementation omitted for brevity

    def update(self):
        """Sends an update request to all the views."""
        # Implementation omitted for brevity

    def is_key_down(self, letter):
        return False

    def is_lamp_on(self, letter):
        return False

    def key_pressed(self, letter):
        # Implementation omitted for brevity
        self.update()

    def key_released(self, letter):
        # Implementation omitted for brevity
        self.update()

    def get_rotor_letter(self, index):
        return "A"

    def rotor_clicked(self, index):
        # Implementation omitted for brevity
        self.update()

def enigma():
    """Runs the Enigma simulator."""
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)