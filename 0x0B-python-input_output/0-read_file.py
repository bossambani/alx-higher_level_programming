#!/usr/bin/python3
"""read file function module"""


def read_file(filename=""):
    """
        Args: filename is the name of the file to be read

        Returns: prints the file content
    """
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
