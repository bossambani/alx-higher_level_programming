#!/usr/bin/python3
"""defines a function that checks if the object is an istance of a class
   that inherited from the specified class.
"""


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
