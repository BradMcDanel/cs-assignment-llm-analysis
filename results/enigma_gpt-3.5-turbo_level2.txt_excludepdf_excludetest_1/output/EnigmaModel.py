# File: EnigmaModel.py

from EnigmaView import EnigmaView

class EnigmaModel:
    def __init__(self):
        """Creates a new EnigmaModel with no views."""
        self._views = []
        self._key_states = {letter: False for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}  # Dictionary to store key states
        self._lamp_states = {letter: False for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}  # Dictionary to store lamp states
        self._rotors = [EnigmaRotor(ROTOR_PERMUTATIONS[i]) for i in range(3)]  # Create rotor objects

    def add_view(self, view):
        """Adds a view to this model."""
        self._views.append(view)

    def update(self):
        """Sends an update request to all the views."""
        for view in self._views:
            view.update()

    def key_pressed(self, letter):
        self._key_states[letter] = True  # Update key state
        self.update()

    def key_released(self, letter):
        self._key_states[letter] = False  # Update key state
        self.update()

    def is_key_down(self, letter):
        return self._key_states[letter]  # Return key state

    def is_lamp_on(self, letter):
        return self._lamp_states[letter]  # Return lamp state

    def rotor_clicked(self, index):
        self._rotors[index].advance()  # Advance the specified rotor
        self.update()

    def get_rotor_letter(self, index):
        return self._rotors[index].get_current_letter()  # Get the letter in the rotor window

class EnigmaRotor:
    def __init__(self, permutation):
        self._permutation = permutation
        self._offset = 0

    def get_offset(self):
        return self._offset

    def get_permutation(self):
        return self._permutation

    def advance(self):
        self._offset = (self._offset + 1) % 26

    def get_current_letter(self):
        return self._permutation[self._offset]

def enigma():
    """Runs the Enigma simulator."""
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

# Startup code

if __name__ == "__main__":
    enigma()