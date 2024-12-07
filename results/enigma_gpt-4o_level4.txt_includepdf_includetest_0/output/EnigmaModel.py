from EnigmaView import EnigmaView
from EnigmaConstants import ALPHABET, ROTOR_PERMUTATIONS, REFLECTOR_PERMUTATION

class EnigmaRotor:
    def __init__(self, permutation):
        self._permutation = permutation
        self._offset = 0
        self._inverse_permutation = self._invert_permutation(permutation)

    def _invert_permutation(self, permutation):
        inverse = [''] * 26
        for i, letter in enumerate(permutation):
            inverse[ord(letter) - ord('A')] = chr(i + ord('A'))
        return ''.join(inverse)

    def get_offset(self):
        return self._offset

    def get_permutation(self, reverse=False):
        return self._inverse_permutation if reverse else self._permutation

    def advance(self):
        self._offset = (self._offset + 1) % 26
        return self._offset == 0

class EnigmaModel:
    def __init__(self):
        self._views = []
        self._keys_state = {letter: False for letter in ALPHABET}
        self._lamps_state = {letter: False for letter in ALPHABET}
        self._rotors = [EnigmaRotor(ROTOR_PERMUTATIONS[i]) for i in range(3)]

    def add_view(self, view):
        self._views.append(view)

    def update(self):
        for view in self._views:
            view.update()

    def key_pressed(self, letter):
        self._keys_state[letter] = True
        self._lamps_state = {l: False for l in ALPHABET}
        lamp_letter = self._encrypt_letter(letter)
        self._lamps_state[lamp_letter] = True
        self.update()

    def key_released(self, letter):
        self._keys_state[letter] = False
        self.update()

    def is_key_down(self, letter):
        return self._keys_state[letter]

    def is_lamp_on(self, letter):
        return self._lamps_state[letter]

    def rotor_clicked(self, index):
        self._rotors[index].advance()
        self.update()

    def get_rotor_letter(self, index):
        offset = self._rotors[index].get_offset()
        return ALPHABET[offset]

    def _encrypt_letter(self, letter):
        index = ALPHABET.index(letter)
        for rotor in reversed(self._rotors):
            index = (index + rotor.get_offset()) % 26
            index = ALPHABET.index(rotor.get_permutation()[index])
            index = (index - rotor.get_offset()) % 26

        index = ALPHABET.index(REFLECTOR_PERMUTATION[index])

        for rotor in self._rotors:
            index = (index + rotor.get_offset()) % 26
            index = ALPHABET.index(rotor.get_permutation(reverse=True)[index])
            index = (index - rotor.get_offset()) % 26

        self._rotors[-1].advance()
        for i in range(len(self._rotors) - 1, 0, -1):
            if self._rotors[i].get_offset() == 0:
                if not self._rotors[i - 1].advance():
                    break

        return ALPHABET[index]

def enigma():
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

if __name__ == "__main__":
    enigma()