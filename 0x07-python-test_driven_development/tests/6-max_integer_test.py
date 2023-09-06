#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    test for max_integer function
    """

    def test_mixed_integer(self):
        self.assertEqual(max_integer([5, -2, 100, 3]), 100)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_repeated_number(self):
        self.assertEqual(max_integer([1000, 1000, 1000]), 1000)

    def test_max_float_numbers(self):
        self.assertEqual(max_integer([3.14, 1.5, 2.7]), 3.14)

    def test_integer_single_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_max_negative_number(self):
        self.assertEqual(max_integer([-5, -2, -8, -1]), -1)

    def test_zero_number(self):
        self.assertEqual(max_integer([0, 0]), 0)

    def test_list_with_string(self):
        with self.assertRaises(TypeError):
            max_integer([0, '1'])

    def test_dict(self):
        with self.assertRaises(KeyError):
            max_integer({'key1': 1, 'key2': 2})

    if __name__ == '__main__':
        unittest.main()
