# Continue from previous code...

    def is_lamp_on(self, letter):
        return self._key_states.get(letter, False)  # Lamps light up when keys are pressed