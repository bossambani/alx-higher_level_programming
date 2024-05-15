#!/usr/bin/python3
"""Defines a class that inherits from list"""


class MyList(list):

    def print_sorted(self):
        """
            Args:
                list: superclass for MyList class
        """
        print(sorted(self))
