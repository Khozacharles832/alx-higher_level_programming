#!/usr/bin/python3
"""unittests for the max_integer function"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.Testcode):
    """A class definition of the unit tests"""
    def test_ordered_list(self):
        """An ordered list test"""
        ordered_list = [1, 2, 3, 4]
        self.asserEqual(max_integer(ordered_list), 4)
    
    def test_unordered_list(self):
        """unit test for an unordered list"""
        unordered_list = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered_list), 4)

    def test_max_at_beginning(self):
        """unit test"""
        max_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_beginning), 4)

    def test_empty_list(self):
        """test for an empty list"""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """test for a list with a single element"""
        single = [8]
        self.assertEqual(max_integer(single), 8)

    def test_float(self):
        """unittests for floats"""
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)

    def test_ints_and_floats(self):
        """test for both ints ans floats"""
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def test_string(self):
        """test a string"""
        string = "Charlie"
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_strings(self):
        """unit test for a list of strings"""
        strings = ["Charlie", "is", "my", "name"]
        self.assertEqual(max_integer(strings), 'name')

    def test_empty_string(self):
        """test an empty string"""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()

