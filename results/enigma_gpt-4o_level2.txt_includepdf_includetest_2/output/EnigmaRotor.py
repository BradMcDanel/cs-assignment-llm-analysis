class EnigmaRotor:
    # ... existing code ...

    def advance(self):
        self._offset = (self._offset + 1) % 26
        return self._offset == 0  # Return True if full revolution occurs

# Update key_pressed in EnigmaModel to handle rotor advancement

class EnigmaModel:
    # ... existing code ...

    def key_pressed(self, letter):
        self._key_states[letter] = True
        carry = self._rotors[2].advance()  # Fast rotor always advances
        if carry:
            carry = self._rotors[1].advance()  # Medium rotor advances if fast rotor completes cycle
        if carry:
            self._rotors[0].advance()  # Slow rotor advances if medium rotor completes cycle
        # ... encryption logic ...
        self.update()