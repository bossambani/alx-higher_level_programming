#!/usr/bin/python3
"""Defines ``BaseGeometry`` class"""


class BaseGeometry:
    """
    Class with def area() method
    """
    def area(self):
        """
        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value to be an integer greater than 0.

        Args:
            name (str): The name of the value being validated.
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
