class EnigmaModel:

    def __init__(self):
        """Creates a new EnigmaModel with no views."""
        self._views = []

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
        # Implement code to respond when a key is pressed
        # Update the rotor and lamps accordingly
        self.update()

    def key_released(self, letter):
        # Implement code to respond when a key is released
        # Update the rotor and lamps accordingly
        self.update()

    def get_rotor_letter(self, index):
        return "A"

    def rotor_clicked(self, index):
        # Implement code to respond when a rotor is clicked
        # Advance the rotor and update the view
        self.update()

def enigma():
    """Runs the Enigma simulator."""
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

if __name__ == "__main__":
    enigma()