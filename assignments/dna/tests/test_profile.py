import unittest
import subprocess

class DNAProfilerTestCase(unittest.TestCase):
    def test_match_alice(self):
        output = subprocess.check_output(["python", "profile.py", "data.csv", "alice.txt"])
        self.assertEqual(output.strip(), b"Alice")

    def test_match_bob(self):
        output = subprocess.check_output(["python", "profile.py", "data.csv", "bob.txt"])
        self.assertEqual(output.strip(), b"Bob")

    def test_match_charlie(self):
        output = subprocess.check_output(["python", "profile.py", "data.csv", "charlie.txt"])
        self.assertEqual(output.strip(), b"Charlie")

    def test_no_match(self):
        output = subprocess.check_output(["python", "profile.py", "data.csv", "nomatch.txt"])
        self.assertEqual(output.strip(), b"No match")

if __name__ == '__main__':
    unittest.main()
