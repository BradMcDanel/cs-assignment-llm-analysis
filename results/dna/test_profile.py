import unittest
from unittest.mock import patch
from profile import longest_run, match_dna

class TestDNAProfile(unittest.TestCase):
    
    def test_longest_run(self):
        self.assertEqual(longest_run("AGATAGATAGATAGATC", "AGAT"), 4)
        self.assertEqual(longest_run("AATGAATGAATG", "AATG"), 3)
        self.assertEqual(longest_run("TATCTATCTATCTATC", "TATC"), 4)
    
    @patch('builtins.open')
    @patch('csv.DictReader')
    def test_match_dna(self, mock_csv_dict_reader, mock_open):
        mock_open.return_value.__enter__.return_value = mock_open
        mock_csv_dict_reader.return_value = iter([
            {"name": "Alice", "AGAT": "5", "AATG": "2", "TATC": "8"},
            {"name": "Bob", "AGAT": "3", "AATG": "7", "TATC": "4"},
            {"name": "Charlie", "AGAT": "6", "AATG": "1", "TATC": "5"}
        ])

        sequence = "AGACGGGTTACCATGACTATCTATCTATCTATCTATCTATCTATCTATCACGTACGTACGTATCGAGATAGATAGATAGATAGATCCTCGACTTCGATCGCAATGAATGCCAATAGACAAAA"
        self.assertEqual(match_dna("fake_database.csv", sequence), "Alice")

        sequence = "AACCCTGCGCGCGCGCGATCTATCTATCTATCTATCCAGCATTAGCTAGCATCAAGATAGATAGATGAATTTCGAAATGAATGAATGAATGAATGAATGAATG"
        self.assertEqual(match_dna("fake_database.csv", sequence), "Bob")

        sequence = "CCAGATAGATAGATAGATAGATAGATGTCACAGGGATGCTGAGGGCTGCTTCGTACGTACTCCTGATTTCGGGGATCGCTGACACTAATGCGTGCGAGCGGATCGATCTCTATCTATCTATCTATCTATCCTATAGCATAGACATCCAGATAGATAGATC"
        self.assertEqual(match_dna("fake_database.csv", sequence), "Charlie")

        sequence = "GGTACAGATGCAAAGATAGATAGATGTCGTCGAGCAATCGTTTCGATAATGAATGAATGAATGAATGAATGAATGACACACGTCGATGCTAGCGGCGGATCGTATATCTATCTATCTATCTATCAACCCCTAG"
        self.assertEqual(match_dna("fake_database.csv", sequence), "No match")

if __name__ == '__main__':
    unittest.main()