#!/usr/bin/python3
""" A class that inherits from list"""


class MyList(list):
    """ my_list class """
    def print_sorted(self):
        """ prints the list in sorted fomart """
        print(sorted(self))
