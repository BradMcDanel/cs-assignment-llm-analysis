import unittest
from EnigmaModel import EnigmaModel

class TestEnigmaModel(unittest.TestCase):
    def setUp(self):
        self.enigma = EnigmaModel()

    def test_encrypt_letter(self):
        # Test that the letter 'A' is correctly encrypted with the initial rotor settings
        encrypted_letter = self.enigma.handle_key_press('A')
        self.assertNotEqual(encrypted_letter, 'A', "Encrypted letter should not be the same as the input.")

    def test_rotor_advancement(self):
        # Test that the fast rotor advances after a key press
        initial_rotor_letter = self.enigma.rotors[-1].get_encryption_letter('A')
        self.enigma.handle_key_press('A')
        advanced_rotor_letter = self.enigma.rotors[-1].get_encryption_letter('A')
        self.assertNotEqual(initial_rotor_letter, advanced_rotor_letter, "Rotor did not advance correctly.")

if __name__ == '__main__':
    unittest.main()