#!/usr/bin/python3
"""Defines class Student"""


class Student:
    """
    defines a tudent by first_name, last_name and age.
    """


    def __init__(self, first_name, last_name, age):
        """
        Initializes a new student instane.

        Args:
            first_name (Str): The first name of the student
            last_name (str): The last name of the student
            age (int): The age of the student
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns:
            dict: a dictionary representation of the student
        """
        return self.__dict__
