#!/usr/bin/python3
"""Defines a function that returns the list of attributes and methods"""


def lookup(obj):
    """
        Args: obj is the argument passed to the function
        Return: The available attributes and methods of the object
    """
    return dir(obj)
