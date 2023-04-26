import unittest
from main import calculate_total


class TestCalculateTotal(unittest.TestCase):

    def test_nj_wic_food(self):
        state = 'NJ'
        items = [{'name': 'Apple', 'type': 'Wic Eligible food', 'price': 1.0},
                 {'name': 'Banana', 'type': 'Wic Eligible food', 'price': 2.0}]
        expected_total = 3.0
        self.assertEqual(calculate_total(state, items), expected_total)

    def test_pa_wic_food(self):
        state = 'PA'
        items = [{'name': 'Apple', 'type': 'Wic Eligible food', 'price': 1.0},
                 {'name': 'Banana', 'type': 'Wic Eligible food', 'price': 2.0}]
        expected_total = 3.0
        self.assertEqual(calculate_total(state, items), expected_total)

    def test_de_wic_food(self):
        state = 'DE'
        items = [{'name': 'Apple', 'type': 'Wic Eligible food', 'price': 1.0},
                 {'name': 'Banana', 'type': 'Wic Eligible food', 'price': 2.0}]
        expected_total = 3.0
        self.assertEqual(calculate_total(state, items), expected_total)

    def test_nj_clothing_no_fur(self):
        state = 'NJ'
        items = [{'name': 'T-shirt', 'type': 'Clothing', 'price': 10.0}]
        expected_total = 10.66
        self.assertEqual(calculate_total(state, items), expected_total)

    def test_nj_clothing_with_fur(self):
        state = 'NJ'
        items = [{'name': 'Fur coat', 'type': 'Clothing', 'price': 1000.0}]
        expected_total = 1066.0
        self.assertEqual(calculate_total(state, items), expected_total)


if __name__ == '__main__':
    unittest.main()
