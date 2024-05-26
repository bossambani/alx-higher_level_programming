#!/usr/bin/python3
""" define a class"""


class Base:
    """Defines class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

