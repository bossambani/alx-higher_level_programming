#!/usr/bin/python3
"""Defines a function that checks the instance of object"""


def is_same_class(obj, a_class):
    """
    Args:
        obj: object whose instance is to be checked
        a_class: instance
    """
    if type(obj) == a_class:
        return True
    else:
        return False
