#!/usr/python3
''' The ``max_integers`` unnittest'''


import unnittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    '''unittest class'''
    def test_max_integer(self):
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([3]), 3)
        self.assertEqual(max_integer([-3]), -3)
        self.assertEqual(max_integer([-1, -2, -4]), -1)
        self.assertEqual(max_integer([15, 10, 5]), 15)
        self.assertEqual(max_integer([15, 10, 5, -15, 15]), 15)
        self.assertEqual(max_integer([15, 15, 15]), 15)
    def test_type_error(self):
        self.assertRaises(TypeError, max_integer, ['h', 1])
        self.assertRaises(TypeError, max_integer, [2, [2, 2]])