#!/usr/bin/python3
"""Defines a function that checks for instance of class that inherits from"""


def is_kind_of_class(obj, a_class):
    """
        Args:
            obj: object that is being inherited
            a_class: instance
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
