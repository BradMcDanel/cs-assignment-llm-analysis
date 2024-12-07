from EnigmaView import EnigmaView
from EnigmaConstants import ROTOR_PERMUTATIONS, REFLECTOR_PERMUTATION


class EnigmaRotor:
    def __init__(self, permutation):
        self.permutation = permutation
        self.inverse_permutation = self._invert_permutation(permutation)
        self.offset = 0

    def _invert_permutation(self, permutation):
        inverse = [''] * 26
        for i, char in enumerate(permutation):
            inverse[ord(char) - ord('A')] = chr(i + ord('A'))
        return ''.join(inverse)

    def get_offset(self):
        return self.offset

    def get_permutation(self):
        return self.permutation

    def get_inverse_permutation(self):
        return self.inverse_permutation

    def advance(self):
        self.offset = (self.offset + 1) % 26
        return self.offset == 0


class EnigmaModel:
    def __init__(self):
        self._views = []
        self.keys = {chr(i + 65): False for i in range(26)}
        self.lamps = {chr(i + 65): False for i in range(26)}
        self.rotors = [EnigmaRotor(perm) for perm in ROTOR_PERMUTATIONS]

    def add_view(self, view):
        self._views.append(view)

    def update(self):
        for view in self._views:
            view.update()

    def key_pressed(self, letter):
        self.keys[letter] = True
        self._encrypt_letter(letter)
        self.update()

    def key_released(self, letter):
        self.keys[letter] = False
        self.lamps = {k: False for k in self.lamps}  # Turn off all lamps
        self.update()

    def is_key_down(self, letter):
        return self.keys.get(letter, False)

    def is_lamp_on(self, letter):
        return self.lamps.get(letter, False)

    def rotor_clicked(self, index):
        self.rotors[index].advance()
        self.update()

    def get_rotor_letter(self, index):
        return chr((self.rotors[index].get_offset() + ord('A')) % 26 + ord('A'))

    def _encrypt_letter(self, letter):
        index = ord(letter) - ord('A')
        # Advance the fast rotor
        carry = self.rotors[0].advance()
        if carry:
            carry = self.rotors[1].advance()
            if carry:
                self.rotors[2].advance()

        # Pass through the rotors right to left
        for rotor in self.rotors:
            index = (index + rotor.get_offset()) % 26
            char = rotor.get_permutation()[index]
            index = (ord(char) - ord('A') - rotor.get_offset()) % 26

        # Reflect
        index = (ord(REFLECTOR_PERMUTATION[index]) - ord('A')) % 26

        # Pass back through the rotors left to right
        for rotor in reversed(self.rotors):
            index = (index + rotor.get_offset()) % 26
            char = rotor.get_inverse_permutation()[index]
            index = (ord(char) - ord('A') - rotor.get_offset()) % 26

        # Set the lamp
        encrypted_letter = chr(index + ord('A'))
        self.lamps[encrypted_letter] = True


def enigma():
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)


if __name__ == "__main__":
    enigma()