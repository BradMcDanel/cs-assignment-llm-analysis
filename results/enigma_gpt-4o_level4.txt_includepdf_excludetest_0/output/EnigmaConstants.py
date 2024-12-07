# File: EnigmaConstants.py

"""This module defines the constants used in the Enigma simulator."""

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # The letters of the alphabet

# The number of rotors
N_ROTORS = 3

# Permutations for each rotor, representing the wiring of the Enigma machine
ROTOR_PERMUTATIONS = [
    "EKMFLGDQVZNTOWYHXUSPAIBRCJ",  # Permutation for slow rotor
    "AJDKSIRUXBLHWTMCQGZNPYFVOE",  # Permutation for medium rotor
    "BDFHJLCPRTXVZNYEIWGAKMUSQO"   # Permutation for fast rotor
]

# Reflector permutation (fixed)
REFLECTOR_PERMUTATION = "IXUHFEZDAOMTKQJWNSRLCYPBVG"