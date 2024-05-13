#!/usr/bin/python3
"""Defines a function that print a list sorted in ascending"""


class MyList(list):
    """
        Args: list is the subclass of MyList
    """
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
