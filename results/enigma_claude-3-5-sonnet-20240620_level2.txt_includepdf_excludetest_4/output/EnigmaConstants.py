# File: EnigmaConstants.py

"""This module defines the constants used in the Enigma simulator."""

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"   # The letters of the alphabet

# It is worth noting that the number of rotors cannot be changed
# without making significant changes to the EnigmaView.py class,
# which assumes that there are exactly three rotors to match the
# top-view image of the machine.

N_ROTORS = 3                              # The number of rotors

# The early German Enigma machines include three rotors, which advance
# at different speeds.  The rotor on the right is the "fast" rotor,
# which advances on every keystroke.  The rotor in the middle is the
# "medium" rotor, which advances when the fast rotor has made a
# complete revolution.  The rotor at the left is the "slow" rotor,
# which advances when the medium rotor has made a complete cycle.
# The ROTOR_PERMUTATION array lists the three rotors from left to
# right: the slow rotor, the medium rotor, and the fast rotor.
#
# Each rotor implements a letter-substitution cipher, which is
# represented by a string of 26 uppercase letters that shows how
# the letters in the alphabet are mapped to new letters as the
# internal signal flows across the rotor from right to left.  For
# example, the slow rotor corresponds to the following mapping
# when it is in its initial position:
#
#    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
#    | | | | | | | | | | | | | | | | | | | | | | | | | |
#    E K M F L G D Q V Z N T O W Y H X U S P A I B R C J

ROTOR_PERMUTATIONS = [
    "EKMFLGDQVZNTOWYHXUSPAIBRCJ",  # Permutation for slow rotor      
    "AJDKSIRUXBLHWTMCQGZNPYFVOE",  # Permutation for medium rotor    
    "BDFHJLCPRTXVZNYEIWGAKMUSQO"   # Permutation for fast rotor      
]

# To the left of the slow rotor, the Enigma machine includes a
# component called the "reflector," which implements a fixed
# permutation that remains unchanged as the rotors advance.  The
# constant REFLECTOR_PERMUTATION defines the mapping of the reflector.
# Note that the reflector is symmetric.  If A is transformed to I,
# then I is transformed to A.

REFLECTOR_PERMUTATION = "IXUHFEZDAOMTKQJWNSRLCYPBVG"
