#!/usr/bin/python3
"""Defines a function that print a list sorted in ascending"""


class MyList(list):

    def print_sorted(self):
        """
            Args: MyList is the subclass of list
        """
        sorted_list = sorted(self)
        print(sorted_list)
