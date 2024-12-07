# Modify the existing functions for milestone #2

def is_lamp_on(self, letter):
    return self._key_states.get(letter, False)  # Lamp on if key is down