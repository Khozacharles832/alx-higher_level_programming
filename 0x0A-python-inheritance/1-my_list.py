#!/usr/bin/python3
"""
module with class my list
"""


class MyList(list):
    """defines the print_sorted method"""
    pass

    def print_sorted(self):
        """a method to sort a list"""

        print(sorted(list(self)))
