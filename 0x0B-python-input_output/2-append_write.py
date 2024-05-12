#!/usr/bin/python3
""" Defines a function that appends data to a file"""


def append_write(filename="", text=""):
    """
        Args: filename is te name of the file to be appended
              text is the data that is to be appended to the file

        Returns: The number of characters written
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        file.write(text)
        return len(text)
