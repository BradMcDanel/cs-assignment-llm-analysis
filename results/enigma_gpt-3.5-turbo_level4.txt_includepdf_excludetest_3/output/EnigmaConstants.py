"""This module defines the constants used in the Enigma simulator."""

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"   # The letters of the alphabet
N_ROTORS = 3  # The number of rotors

ROTOR_PERMUTATIONS = [
    "EKMFLGDQVZNTOWYHXUSPAIBRCJ",  # Permutation for slow rotor
    "AJDKSIRUXBLHWTMCQGZNPYFVOE",  # Permutation for medium rotor
    "BDFHJLCPRTXVZNYEIWGAKMUSQO"   # Permutation for fast rotor
]

REFLECTOR_PERMUTATION = "IXUHFEZDAOMTKQJWNSRLCYPBVG"