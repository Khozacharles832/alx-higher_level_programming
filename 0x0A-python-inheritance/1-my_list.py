#!/usr/bin/python3
"""
module with class my list
"""


class MyList(list):
    """defines the print_sorted method"""
    pass

    def print_sorted(self):
        """a method to sort a list"""
        sorted_list = sorted(self)
        print(sorted_list)
