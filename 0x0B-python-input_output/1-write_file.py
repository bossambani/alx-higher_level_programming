#!/usr/bin/python3
"""Defines a function that writes to a file"""


def write_file(filename="", text=""):
    """
        args: filename is the name of the file to be written onto
              text is the text to be written on the file

        Returns: The number of characters written
    """
    with open(filename, mode="w", encoding='utf-8') as file:
        file.write(text)
    return len(text)
