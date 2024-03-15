import unittest
from unittest.mock import patch
from food_web_analyzer import read_food_web, find_apex_predators, find_producers, find_flexible_eaters, find_tastiest, calculate_heights

class TestFoodWebAnalyzer(unittest.TestCase):
    @patch('builtins.open', unittest.mock.mock_open(read_data="Lion,Zebra\nZebra,Grass\n"))
    def test_read_food_web(self):
        expected = {'Lion': ['Zebra'], 'Zebra': ['Grass']}
        self.assertEqual(read_food_web('fake_file.txt'), expected)
    
    def test_find_apex_predators(self):
        food_web = {'Lion': ['Zebra'], 'Zebra': ['Grass']}
        self.assertEqual(find_apex_predators(food_web), ['Lion'])
    
    def test_find_producers(self):
        food_web = {'Lion': ['Zebra'], 'Zebra': ['Grass']}
        self.assertEqual(find_producers(food_web), ['Grass'])
    
    def test_find_flexible_eaters(self):
        food_web = {'Lion': ['Zebra', 'Gazelle'], 'Cheetah': ['Gazelle']}
        self.assertEqual(find_flexible_eaters(food_web), ['Lion'])
    
    def test_find_tastiest(self):
        food_web = {'Lion': ['Zebra'], 'Cheetah': ['Zebra']}
        self.assertEqual(find_tastiest(food_web), ['Zebra'])
    
    def test_calculate_heights(self):
        food_web = {'Lion': ['Zebra'], 'Zebra': ['Grass'], 'Grass': []}
        expected = {'Lion': 2, 'Zebra': 1, 'Grass': 0}
        self.assertEqual(calculate_heights(food_web), expected)

if __name__ == '__main__':
    unittest.main()