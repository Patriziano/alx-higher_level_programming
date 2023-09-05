#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    """Suite test for max_integer function"""

    def test_empty_list(self):
        self.assertIsNone(max_integer([]), None)

    def test_single_element_list(self):
        self.assertEqual(max_integer([42]), 42)

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 2, 0, -4, 5]), 5)

    def test_duplicate_numbers(self):
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_mixed_data_types(self):
        with self.assertRaises(TypeError):
            max_integer([1, '2', 3, 4, 5])

    def test_list_with_loop(self):
        my_list = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer([i * 5 for i in my_list]), 25)

    def test_one_number_in_a_list(self):
        self.assertEqual(max_integer([1]), 1)

    def test_string_number_in_a_list(self):
        with self.assertRaises(TypeError):
            max_integer([0, '1'])

    def test_tuple_in_a_list(self):
        with self.assertRaises(TypeError):
            max_integer([10, (20, 30)])

    def test_dictionary(self):
        with self.assertRaises(KeyError):
            max_integer({'key1': 1, 'key2': 2})

    def test_number(self):
        with self.assertRaises(TypeError):
            max_integer(1)


    def test_big_numbers(self):
        self.assertEqual(max_integer([104, 542, 472, 612, 419, 666, 777, 190,
            831, 428, 272, 253, 1065, 146, 235, 317, 453, 671, 942, 1022, 456,
            568, 1041, 465, 128, 864, 234]), 1065)
if __name__ == '__main__':
    unittest.main()
