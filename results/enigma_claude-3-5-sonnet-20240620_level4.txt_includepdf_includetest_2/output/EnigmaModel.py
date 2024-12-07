from EnigmaView import EnigmaView
from EnigmaRotor import EnigmaRotor
from EnigmaConstants import ALPHABET, N_ROTORS, ROTOR_PERMUTATIONS, REFLECTOR_PERMUTATION

class EnigmaModel:
    def __init__(self):
        self._views = []
        self._keys_down = {letter: False for letter in ALPHABET}
        self._lamps_on = {letter: False for letter in ALPHABET}
        self._rotors = [EnigmaRotor(ROTOR_PERMUTATIONS[i]) for i in range(N_ROTORS)]
        self._reflector = REFLECTOR_PERMUTATION

    def add_view(self, view):
        self._views.append(view)

    def update(self):
        for view in self._views:
            view.update()

    def is_key_down(self, letter):
        return self._keys_down[letter]

    def is_lamp_on(self, letter):
        return self._lamps_on[letter]

    def key_pressed(self, letter):
        self._keys_down[letter] = True
        self._advance_rotors()
        encrypted_letter = self._encrypt(letter)
        self._lamps_on[encrypted_letter] = True
        self.update()

    def key_released(self, letter):
        self._keys_down[letter] = False
        for lamp in ALPHABET:
            self._lamps_on[lamp] = False
        self.update()

    def get_rotor_letter(self, index):
        return self._rotors[index].get_visible_letter()

    def rotor_clicked(self, index):
        self._rotors[index].advance()
        self.update()

    def _advance_rotors(self):
        carry = True
        for rotor in reversed(self._rotors):
            if carry:
                carry = rotor.advance()
            else:
                break

    def _encrypt(self, letter):
        signal = ALPHABET.index(letter)
        
        # Right to left through rotors
        for rotor in reversed(self._rotors):
            signal = rotor.apply_forward(signal)
        
        # Through reflector
        signal = ALPHABET.index(self._reflector[signal])
        
        # Left to right through rotors
        for rotor in self._rotors:
            signal = rotor.apply_backward(signal)
        
        return ALPHABET[signal]

def enigma():
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

if __name__ == "__main__":
    enigma()