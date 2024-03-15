import unittest
from unittest.mock import patch
import police_shootings

class TestPoliceShootings(unittest.TestCase):

    def setUp(self):
        self.database = {
            1694: {'name': 'John Doe', 'state': 'MN', 'race': 'B'},
            1700: {'name': 'Jane Smith', 'state': 'TX', 'race': 'W'}
        }

    @patch('police_shootings.read_data')
    def test_find_by_id(self, mock_read_data):
        mock_read_data.return_value = self.database
        self.assertEqual(police_shootings.find_by_id(self.database, 1694), 'John Doe')
        self.assertEqual(police_shootings.find_by_id(self.database, 9999), 'Not Found')

    def test_find_by_state(self):
        self.assertEqual(police_shootings.find_by_state(self.database, 'MN'), ['John Doe'])

    def test_count_by_race(self):
        expected_counts = {'B': 1, 'W': 1}
        self.assertEqual(police_shootings.count_by_race(self.database), expected_counts)

    def test_calculate_fraction(self):
        race_counts = {'B': 1, 'W': 1}
        self.assertAlmostEqual(police_shootings.calculate_fraction(race_counts, 'B'), 0.5)

if __name__ == '__main__':
    unittest.main()