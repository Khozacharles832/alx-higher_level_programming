#!/usr/bin/python3
'''
The max integer unittest module
'''


import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    '''Unittest for the max-integer module'''
    def setup(self):
        self.ordered_list = [1, 2, 3, 4]
        self.unordered_list = [1, 3, 4, 2]

    def test_max(self):
        self.assertEqual(max_integer(self.ordered_list),
                max_integer(self.unordered_list))

    def test_string(self):
        self.assertEqual(max_integer('string'), 't')

    def test_nothing(self):
        self.assertEqual(max_integer(), None)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_list_of_negatives(self):
        self.assertEqual(max_integer([-2, -5, -7, -8]), -2)

    def test_key_error(self):
        with self.assertRaises(KeyError):
            max_integer({5 : 6})

    def test_type_error_too_many_args(self):
        with self.assertRaises(TypeError):
            max_integer('tuple', 'ofstrings')

    def test_type_error_on_incoparable_list_items(self):
        with self.assertRaises(TypeError):
            max_integer([[], {}])
