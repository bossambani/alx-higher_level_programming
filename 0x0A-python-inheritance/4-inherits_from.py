#!/usr/bin/python3
"""Defines ``inherits_from`` method"""


def inherits_from(obj, a_class):
    """
        Args:
            obj: object that is being checked
            a_class: class to check against
        Returns:
            True if obj is an instance of a subclass of class, False otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
