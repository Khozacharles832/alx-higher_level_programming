#!/usr/bin/python3
"""unittests for the max_integer function"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """A class definition of the unit tests"""

    def test_other(self):
        '''unit test for the bigger half'''
        self.assertEqual(max_integer([6, 7, 8, 9]), 9)

    def test_empty(self):
        '''unit test for empty list'''
        self.assertEqual(max_integer([]), None)

    def test_single(self):
        '''Test for one item in list'''
        self.assertEqual(max_integer([3]), 3)

    def test_one_neg(self):
        '''Test for one negative item'''
        self.assertEqual(max_integer([-3]), -3)

    def test_neg(self):
        '''Test with negative values'''
        self.assertEqual(max_integer([3, -2, -7, -9]), 3)

    def test_unorderd(self):
        '''Test with unorderd list'''
        self.assertEqual(max_integer([2, 4, 6, 0, 5, 3]), 6)

if __name__ == '__main__':
    unittest.main()
